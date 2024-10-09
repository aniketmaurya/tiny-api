# main.py
from tiny_api import TinyAPI
from starlette.responses import JSONResponse

app = TinyAPI()


@app.router.get("/")
async def hello(request):
    return JSONResponse({"hello": "world"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
