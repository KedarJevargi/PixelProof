from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from datetime import datetime, timezone

from utils import image, generate_zip_file

router = APIRouter(tags=["Image"])


@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    name: str = Form(...)
):
    # Validate before reading to fail fast
    image.validate_image(file)

    image_bytes = await file.read()

    image_hash = image.hash_image(image_bytes)
    signature = image.sign_hash(image_hash)

    metadata = {
        "hash": image_hash,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "name": name
    }

    # Preserve original file extension
    original_filename = file.filename or "image.jpg"

    container = generate_zip_file.create_container(
        image_bytes, metadata, signature, filename=original_filename
    )

    return StreamingResponse(
        container,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": "attachment; filename=image.ppimg"
        }
    )