import zipfile
from io import BytesIO
import json


def create_container(image_bytes: bytes, metadata: dict, signature: str, filename: str = "image.jpg") -> BytesIO:
    buffer = BytesIO()

    with zipfile.ZipFile(buffer, "w") as zip_file:
        zip_file.writestr(filename, image_bytes)
        zip_file.writestr("metadata.json", json.dumps(metadata))
        zip_file.writestr("signature.sig", signature)

    buffer.seek(0)
    return buffer