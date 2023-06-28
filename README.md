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

4. Check version `./pants --version`
