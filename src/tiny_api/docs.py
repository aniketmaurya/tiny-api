# docs.py
from starlette.responses import JSONResponse
from starlette.routing import Route


def get_openapi_schema(router):
    # Logic to generate OpenAPI schema based on router routes
    return {}


def openapi_route(router):
    async def openapi(request):
        schema = get_openapi_schema(router)
        return JSONResponse(schema)

    return Route("/openapi.json", endpoint=openapi, methods=["GET"])
