# applications.py
from starlette.applications import Starlette

from .routing import APIRouter


class TinyAPI:
    def __init__(self, lifespan=None):
        self.router = APIRouter()
        self._app = None  # Initialize app later
        self.lifespan = lifespan

    def create_app(self):
        self._app = Starlette(routes=self.router.routes, lifespan=self.lifespan)

    def get(self, path, dependencies=None):
        return self.router.get(path)

    def add_api_route(self, path, endpoint, methods, dependencies=None):
        self.router.add_api_route(path, endpoint, methods, dependencies)

    def add_middleware(self, middleware, **kwargs):
        self._app.add_middleware(middleware, **kwargs)

    async def __call__(self, scope, receive, send):
        if not self._app:
            self.create_app()
        await self._app(scope, receive, send)
