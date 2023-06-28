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
