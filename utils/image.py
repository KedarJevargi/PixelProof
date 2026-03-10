from fastapi import HTTPException, status, UploadFile
import hashlib


def validate_image(file:UploadFile):
    MAX_FILE_SIZE=5*1024*1024
    valid_image_type={"image/jpeg", 
                      "image/png"
                      }
    if file.content_type not in valid_image_type:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    elif  file.size>MAX_FILE_SIZE:
        raise HTTPException(status_code=status.HTTP_413_CONTENT_TOO_LARGE)
    

async def hash_image(file: UploadFile):
    image_bytes = await file.read()
    sha256 = hashlib.sha256()
    sha256.update(image_bytes)
    image_hash = sha256.hexdigest()
    await file.seek(0)
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(image_bytes),
        "image_hash": image_hash,
        "status": "Image hashed successfully"
    }
    
