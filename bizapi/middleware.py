from .types import Request, Response


class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.app.handle_request(request)
        return response(environ, start_response)

    def add(self, middleware_class):
        self.app = middleware_class(self.app)

    def request(self, request: Request):
        pass

    def response(self, request: Request, response: Response):
        pass

    def handle_request(self, request: Request):
        self.request(request)
        response = self.app.handle_request(request)
        self.response(request, response)

        return response
