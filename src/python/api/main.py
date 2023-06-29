from fastapi import FastAPI
from utils import get_kst_time  # from common

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/from-common-utils")
def from_common_utils():
    return get_kst_time()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
