from fastapi import FastAPI
from typing import Optional
from post import schemas


app = FastAPI()


@app.get("/posts")
async def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"posts list of {limit} published posts"}
    else:
        return {"data": f"posts list of {limit} posts"}


@app.get("/post/unpublished")
async def unpublished():
    return {"data": "all unpublished posts"}


@app.get("/post/{id}")
async def show(id: int):
    return {"data": id}


@app.get("/post/{id}/applications")
async def comments(limit=10):
    return {"data": {"1", "2"}}


@app.post("/posts")
async def create(post: schemas.Post):
    return post


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
