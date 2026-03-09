from fastapi import APIRouter, UploadFile, File

from utils import image


router = APIRouter(tags=["Image"])


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    return image.validate_image(file)
    