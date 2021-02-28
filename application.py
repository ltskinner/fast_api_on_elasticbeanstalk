
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/example_1")
def read_example_1():
    return {"endpoint": "example_1"}


if __name__ == '__main__':
    app.app.run()
