from jinja2 import FileSystemLoader
from whitenoise import WhiteNoise

from .types import Request, Response
from .router import Router
from .errors import page_not_found, method_not_allowed
from .middleware import Middleware
from . import globals

import inspect
import os


class BizAPI:

    def __init__(self, template_dir: str = 'templates', static_dir: str = 'static'):
        self.__router = Router()
        self.whitenoise = WhiteNoise(self._wsgi_app, root=static_dir, prefix='/static')
        self.exception_handler = None
        self.middleware = Middleware(self)

        globals.template_environment.loader = FileSystemLoader(os.path.abspath(template_dir))

    def __call__(self, environ, start_response):
        path_info = environ['PATH_INFO']
        if path_info.startswith('/static'):
            return self.whitenoise(environ, start_response)
        return self.middleware(environ, start_response)

    def _wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()
        handler_data, kwargs = self.__router.find_handler(request)
        if handler_data is not None:
            handler = handler_data.get(request.method, None)

            if handler is None:
                return method_not_allowed(response)

            if inspect.isclass(handler):
                handler_method = getattr(handler, request.method.lower(), None)
                if handler_method is None:
                    return method_not_allowed(response)
                handler = handler_method
            try:
                handler(request, response, **kwargs)
            except Exception as e:
                if self.exception_handler is not None:
                    self.exception_handler(request, response, e)
                else:
                    raise e
        else:
            return page_not_found(response)
        return response

    def _add_method_route(self, path: str, methods: list = None):
        def wrapper(func):
            self.__router.add_route(path, func, methods)
            return func

        return wrapper

    def route(self, path: str, methods: list = None):
        if methods is None:
            methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT']

        def wrapper(func):
            self.__router.add_route(path, func, methods)
            return func

        return wrapper

    def register_route(self, path: str, handler, methods: list = None):
        if methods is None:
            methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT']
        self.__router.add_route(path, handler, methods)

    def add_exception_handler(self, handler):
        self.exception_handler = handler

    def add_middleware(self, middleware_class):
        self.middleware.add(middleware_class)

    def get(self, path: str):
        return self._add_method_route(path, ['GET'])

    def post(self, path: str):
        return self._add_method_route(path, ['POST'])

    def put(self, path: str):
        return self._add_method_route(path, ['PUT'])

    def patch(self, path: str):
        return self._add_method_route(path, ['PATCH'])

    def delete(self, path: str):
        return self._add_method_route(path, ['DELETE'])

    def head(self, path: str):
        return self._add_method_route(path, ['HEAD'])

    def options(self, path: str):
        return self._add_method_route(path, ['OPTIONS'])

    def trace(self, path: str):
        return self._add_method_route(path, ['TRACE'])

    def connect(self, path: str):
        return self._add_method_route(path, ['CONNECT'])
