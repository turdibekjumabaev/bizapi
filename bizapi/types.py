from webob import Request, Response as WebObResponse

import json


class Response:
    def __init__(self, body=b'', status=None, app_iter=None, content_type=None, conditional_response=None, **kw):
        self.json = None
        self.html = None
        self.text = None
        self.content_type = content_type
        self.body = body if isinstance(body, bytes) else body.encode('utf-8')
        self.status_code = status or 200
        self.app_iter = app_iter
        self.conditional_response = conditional_response
        self.kwargs = kw

    def __call__(self, environ, start_response):
        self.set_body_and_content_type()

        response = WebObResponse(
            body=self.body, content_type=self.content_type, status=str(self.status_code), app_iter=self.app_iter, conditional_response=self.conditional_response
        )

        return response(environ, start_response)

    def set_body_and_content_type(self):
        if self.json is not None:
            self.body = json.dumps(self.json).encode("utf-8")
            self.content_type = "application/json"

        if self.html is not None:
            self.body = self.html.encode()
            self.content_type = "text/html"

        if self.text is not None:
            self.body = self.text
            self.content_type = "text/plain"
