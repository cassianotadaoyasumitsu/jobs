from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"data": {"message": "Hello World"}}


@app.get("/about")
async def about():
    return {"message": "About Page"}
