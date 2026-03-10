from pathlib import Path
from fastapi import HTTPException, status, UploadFile
import hashlib
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

BASE_DIR = Path(__file__).parent


def validate_image(file: UploadFile):
    MAX_FILE_SIZE = 5 * 1024 * 1024
    valid_image_types = {"image/jpeg", "image/png"}

    if file.content_type not in valid_image_types:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)


def hash_image(image_bytes: bytes) -> str:
    sha256 = hashlib.sha256()
    sha256.update(image_bytes)
    return sha256.hexdigest()


def sign_hash(image_hash: str) -> str:
    key_path = BASE_DIR / "keys" / "private.pem"

    with open(key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

    signature = private_key.sign(
        image_hash.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Hex-encode so the .sig file is portable and human-readable
    return signature.hex()