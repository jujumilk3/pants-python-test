from common.utils import function_from_common_utils
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/utils-test")
def utils_test():
    return {"message": function_from_common_utils()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
