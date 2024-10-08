
class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def find_handler(self, request):
        return self.routes.get(request.path)
