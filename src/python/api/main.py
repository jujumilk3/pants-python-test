from fastapi import FastAPI
from common.utils import utcnow


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/common-test")
def common_test():
    return utcnow()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
