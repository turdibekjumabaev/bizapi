from .types import Request, Response
from .router import Router
from .errors import page_not_found


class OneAPI:

    def __init__(self):
        self.router = Router()

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()
        handler = self.router.find_handler(request)
        if handler is not None:
            handler(request, response)
        else:
            return page_not_found()
        return response

    def route(self, path):
        def wrapper(func):
            self.router.add_route(path, func)
            return func
        return wrapper
