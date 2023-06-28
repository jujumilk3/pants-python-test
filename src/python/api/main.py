from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
