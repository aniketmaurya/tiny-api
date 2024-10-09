from functools import wraps
from starlette.routing import Route


class APIRouter:
    def __init__(self):
        self.routes = []

    def add_api_route(self, path, endpoint, methods, dependencies=None):
        route = Route(path, endpoint=endpoint, methods=methods)
        self.routes.append(route)

    def get(self, path):
        return self._create_decorator(path, ["GET"])

    def post(self, path):
        return self._create_decorator(path, ["POST"])

    # Add other HTTP methods as needed

    def _create_decorator(self, path, methods):
        def decorator(func):
            @wraps(func)
            async def endpoint(request):
                return await func(request)

            self.add_api_route(path, endpoint, methods)
            return endpoint

        return decorator
