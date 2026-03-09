from fastapi import FastAPI

from api.image import router

app = FastAPI(description="PixelProof Backend")

app.include_router(router)

@app.get("/health")
def health():
    return {"Status": "Ok"}
