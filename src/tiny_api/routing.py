# routing.py
import inspect

from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request
from pydantic import ValidationError, BaseModel

from functools import wraps


class APIRouter:
    def __init__(self):
        self.routes = []

    def add_api_route(self, path, endpoint, methods, dependencies=None):
        route = Route(path, endpoint=endpoint, methods=methods)
        self.routes.append(route)

    def get(self, path):
        return self._create_decorator(path, ['GET'])

    def post(self, path):
        return self._create_decorator(path, ['POST'])

    # Add other HTTP methods as needed

    def _create_decorator(self, path, methods):
        def decorator(func):
            @wraps(func)
            async def endpoint(request):
                return await func(request)

            self.add_api_route(path, endpoint, methods)
            return endpoint

        return decorator


def _create_decorator(self, path, methods):
    def decorator(func):
        sig = inspect.signature(func)

        @wraps(func)
        async def endpoint(request: Request):
            kwargs = {}
            for name, param in sig.parameters.items():
                if param.annotation == Request:
                    kwargs[name] = request
                elif issubclass(param.annotation, BaseModel):
                    try:
                        data = await request.json()
                        kwargs[name] = param.annotation(**data)
                    except ValidationError as e:
                        return JSONResponse({'errors': e.errors()}, status_code=422)
                else:
                    kwargs[name] = request.path_params.get(name)
            return await func(**kwargs)

        self.add_api_route(path, endpoint, methods)
        return endpoint

    return decorator
