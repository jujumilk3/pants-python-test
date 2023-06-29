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
