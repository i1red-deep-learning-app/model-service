from pydantic import BaseSettings


class S3Settings(BaseSettings):
    bucket_name: str

    class Config:
        env_prefix = "s3_"
