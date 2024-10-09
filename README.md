# Tiny API 🚀

A FastAPI like lean library for building REST APIs.

> Created this project as a temporary replacement of FastAPI for Python 3.13 free-threading support.

## Example:

```python

# main.py
from tiny_api import TinyAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = TinyAPI()


class Item(BaseModel):
    name: str
    price: float


@app.router.get("/")
async def hello(request):
    return JSONResponse({"hello": "world"})


@app.router.post("/items")
async def create_item(item: Item):
    # Process the item
    return JSONResponse({"item": item.model_dump()})


@app.router.get("/items/{item_id}")
async def read_item(item_id: int):
    # Retrieve the item
    return JSONResponse({"item_id": item_id})


if __name__ == "__main__":
    import uvicorn

    app.create_app()

    uvicorn.run(app, host="0.0.0.0", port=8000)
```
