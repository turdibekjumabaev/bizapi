from parse import parse


class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def find_handler(self, request):
        for path, handler in self.routes.items():
            parsed = parse(path, request.path)
            if parsed is not None:
                return handler, parsed.named

        return None, None
