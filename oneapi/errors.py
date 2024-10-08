from webob import Response


def page_not_found():
    response = Response('Not Found', status=404)
    return response
