from fastapi import HTTPException, status, UploadFile
async def validate_image(file:UploadFile):
    MAX_FILE_SIZE=5*1024*1024

    valid_image_type={"image/jpeg", 
                      "image/png"
                      }
    if file.content_type not in valid_image_type:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    elif  len(await file.read())>MAX_FILE_SIZE:
        raise HTTPException(status_code=status.HTTP_413_CONTENT_TOO_LARGE)
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size":file.size,
        "status": "Image accepted"
    }