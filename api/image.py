from fastapi import APIRouter, UploadFile, File

from utils import image


router = APIRouter(tags=["Image"])


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    image.validate_image(file)
    return await  image.hash_image(file)
    