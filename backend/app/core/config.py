from pydantic import BaseSettings


class Settings(BaseSettings):

    MINIO_ENDPOINT: str = "http:///0.0.0.0:9000"

    MINIO_ACCESS_KEY: str = "minioadmin"

    MINIO_SECRET_KEY: str = "minioadmin"

    MINIO_BUCKET: str = "uploads"


settings = Settings()

