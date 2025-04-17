from fastapi import APIRouter, File, UploadFile

from app.storage import upload_to_minio


router = APIRouter()


@router.post("/upload")

async def upload_file(file: UploadFile = File(...)):

    result = await upload_to_minio(file)

    return {"status": "uploaded", "url": result}

