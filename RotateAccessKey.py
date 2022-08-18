import boto3


class RotateAccessKey:
    def __init__(self, access_key_id: str, secret_access_key) -> None:
        self.__iam_client = boto3.client(
            "iam",
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
        )
        self.access_key_id = access_key_id

    def _create_access_key(self) -> dict:
        response = self.__iam_client.create_access_key()
        return response["AccessKey"]

    def _delete_access_key(self) -> dict:
        response = self.__iam_client.delete_access_key(AccessKeyId=self.access_key_id)
        return response

    def rotate_access_keys(self):
        new_access_key = {}
        if new_access_key := self._create_access_key():
            self._delete_access_key()
        return new_access_key
