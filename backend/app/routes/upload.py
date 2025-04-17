from fastapi import APIRouter, File, UploadFile, HTTPException

from minio import Minio

from minio.error import S3Error

import os


# Инициализация MinIO клиента

minio_client = Minio(

    "185.182.219.45:9000",  # Замените на ваш адрес MinIO

    access_key="minioadmin",  # Замените на ваш access key

    secret_key="minioadmin",  # Замените на ваш secret key

    secure=False  # Если не используете SSL

)


bucket_name = "my-bucket"  # Замените на ваш бакет


# Убедитесь, что бакет существует

if not minio_client.bucket_exists(bucket_name):

    minio_client.make_bucket(bucket_name)


router = APIRouter()


@router.post("/upload/")

async def upload_file(file: UploadFile = File(...)):

    try:

        file_location = f"uploads/{file.filename}"

        # Загружаем файл в MinIO

        minio_client.put_object(

            bucket_name, 

            file_location, 

            file.file, 

            file.file._size

        )

        return {"filename": file.filename, "message": "File uploaded successfully"}

    except S3Error as e:

        raise HTTPException(status_code=500, detail=f"Error uploading file: {e}")

