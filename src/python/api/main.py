from fastapi import FastAPI
from utils import get_kst_time  # from common
from api_utils.utils import api_util_function  # from api_utils

from inner.inner_utils import get_kst_time_inner  # from common.common

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/api-util")
def api_util():
    return api_util_function()


@app.get("/from-common-utils")
def from_common_utils():
    return get_kst_time()


@app.get("/from-common-inner-utils")
def from_common_inner_utils():
    return get_kst_time_inner()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
