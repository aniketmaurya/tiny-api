import pytest
from starlette.testclient import TestClient

from starlette.responses import JSONResponse

from tiny_api import TinyAPI


@pytest.fixture
def client():
    # Create a simple app instance
    app = TinyAPI()

    # Define a route directly in the test file
    @app.router.get("/")
    async def hello(request):
        return JSONResponse({"hello": "world"})

    return TestClient(app)


def test_hello_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
