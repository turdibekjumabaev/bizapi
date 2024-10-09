from .types import Response


def page_not_found(response: Response) -> Response:
    response.status = '404 Not Found'
    response.body = b'Not Found'
    return response


def method_not_allowed(response: Response) -> Response:
    response.status = '405 Method Not Allowed'
    response.body = b'Method Not Allowed'
    return response
