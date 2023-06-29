# pants-python-test

## Install

1. Check and choose stable version from <https://pypi.org/project/pantsbuild.pants/#history>
2. Create `pants.toml` file in project root directory

   ```toml
    [GLOBAL]
    pants_version = "2.16.0"

    [anonymous-telemetry]
    enabled = false
   ```

3. Install pants

    ```bash
    curl -L -o ./pants https://pantsbuild.github.io/setup/pants
    chmod +x ./pants
    ```

    or Just install pants binary (<https://www.pantsbuild.org/docs/installation>).  
    **※ They(Creators of pants) recommend to use binary**

4. Check version `./pants --version` or `pants --version`

5. Create projects and fill `pants.toml` file

    ```toml
    [GLOBAL]
    pants_version = "2.16.0"
    backend_packages = [
        "pants.backend.python",
        "pants.backend.python.lint.black",
        "pants.backend.python.lint.isort",
    ]

    [source]
    root_patterns = [
        "src/python/api",
        "src/python/common"
    ]

    [anonymous-telemetry]
    enabled = true
    repo_id = "55e350b1-b251-4bc2-bd52-5a9ac30d2440"
    ```

6. Create some python files in `src/python/api` and `src/python/common` directories.
   `__init__.py` doesn't work. In my case, I created `main.py` files.
7. Run `pants tailor ::` to generate `BUILD` at each directory.
8. Init with `poetry` And fill `BUILD`.
   `src/python/api/BUILD`

   ```python
    python_sources(
        name='api-server'
    )

    poetry_requirements()   
   ```

9. run
    api
    `pants run src/python/api:api-server` or
    `pants run src/python/api/main.py`.
    common
    `pants run src/python/common:lib` or
    `pants run src/python/common/main.py`

10. change api `main.py` as fastapi

    ```python
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
    ```

    and run `pants run src/python/api:api-server` or `pants run src/python/api/main.py`

11. create some util from `common` to use in `api`
12. use function from `common` in `api`
13. run `pants run src/python/api/main.py` and test router `GET /from-common-utils`
14. if you wanna extend utils further with hierarchy structure, create dir and create `BUILD` again by using `pants tailor ::`
15. if you wanna turn on auto renew fastapi server, you have to write pex at `BUILD` file.

    ```toml
    # src/python/api/BUILD
    python_sources(
        name="api-server",
        dependencies=[
            "src/python/common",
        ],
    )


    pex_binary(
        name="api-server2",
        entry_point="main.py",
        dependencies=[
            ":api",
        ],
        restartable=True,
    )

    poetry_requirements()
    ```

    But mostly you will run with uvicorn command at each directory.
