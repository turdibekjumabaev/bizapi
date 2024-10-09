from parse import parse

from .exceptions import RouteAlreadyExistsError


class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path: str, handler, methods: list):
        if path in self.routes:
            raise RouteAlreadyExistsError(path)

        self.routes[path] = {
            'handler': handler,
            'methods': methods
        }

    def find_handler(self, request):
        for path, handler_data in self.routes.items():
            parsed = parse(path, request.path)
            if parsed is not None:
                return handler_data, parsed.named

        return None, None
