
class RouteAlreadyExistsError(Exception):
    def __init__(self, path):
        super().__init__(f"Duplicate route for path: {path}")
