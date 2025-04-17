from boto3.session import Session

from io import BytesIO


session = Session()

s3 = session.client(

    service_name='s3',

    endpoint_url='http://185.182.219.45:9000',

    aws_access_key_id='minioadmin',

    aws_secret_access_key='minioadmin',

)


BUCKET = 'files'


async def upload_to_minio(file):

    content = await file.read()

    s3.put_object(Bucket=BUCKET, Key=file.filename, Body=content)

    return f"http://185.182.219.45:9000/{BUCKET}/{file.filename}"

