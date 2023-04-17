import boto3
from botocore.exceptions import ClientError

from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.data_storage.exceptions import LoadingFailedException, SavingFailedException


class S3DataStorage(AbstractDataStorage):
    def __init__(self, bucket_name: str) -> None:
        self.bucket_name = bucket_name
        self.s3_client = boto3.client("s3")

    def load_file(self, file_key: str) -> bytes:
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_key)
            return response["Body"].read()
        except ClientError as e:
            raise LoadingFailedException(str(e))

    def save_file(self, file_key: str, file_content: bytes) -> None:
        try:
            self.s3_client.put_object(Bucket=self.bucket_name, Key=file_key, Body=file_content)
        except ClientError as e:
            raise SavingFailedException(str(e))
