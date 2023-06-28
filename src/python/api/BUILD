python_sources(
    name="api",
    dependencies=[
        "src/python/common",
    ],
)

pex_binary(
    name="api_pex",
    entry_point="api.main:app",
    dependencies=[":api"],
    restartable=True,
)

poetry_requirements()
