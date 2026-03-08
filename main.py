from fastapi import FastAPI

app = FastAPI(description="PixelProof Backend")

@app.get("/health")
def health():
    return {"Status": "Ok"}