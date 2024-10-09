# TinyAPI 🚀

A FastAPI like lean library for building REST APIs.

> Created this project as a temporary replacement of FastAPI for Python 3.13 free-threading support.

## Example:

```python
from starlette.responses import JSONResponse
import uvicorn
from tiny_api import TinyAPI

app = TinyAPI()

@app.router.get("/")
async def hello(request):
    return JSONResponse({"hello": "world"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
