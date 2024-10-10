from parse import parse

from .types import Request
from .exceptions import RouteAlreadyExistsError


class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path: str, handler, methods: list):
        if path not in self.routes:
            self.routes[path] = {}

        for method in methods:
            if method in self.routes[path]:
                raise RouteAlreadyExistsError(path, method)

            self.routes[path][method] = handler

    def find_handler(self, request: Request):
        for path, handler_data in self.routes.items():
            parsed = parse(path, request.path)
            if parsed is not None:
                return handler_data, parsed.named

        return None, None
