from pydantic import BaseSettings as _BaseSettings


class BaseSettings(_BaseSettings):
    SERVICE_NAME: str
