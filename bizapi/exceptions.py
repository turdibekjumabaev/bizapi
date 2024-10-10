
class RouteAlreadyExistsError(Exception):
    def __init__(self, path, method):
        super().__init__(f"Route for {path} with method {method} already exists")
