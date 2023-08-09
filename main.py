import io

import pytesseract
from fastapi import FastAPI, File
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from PIL import Image

app = FastAPI(title="tesseract-jpn-docker")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/", include_in_schema=False)
async def route_index():
    return RedirectResponse("/docs")


@app.post("/tesseract-jpn", summary="Run OCR on an image.")
async def route_tesseract_jpn(image: bytes = File()):
    return pytesseract.image_to_string(
        image=Image.open(io.BytesIO(image)),
        lang="jpn",
    )


@app.post("/tesseract-jpn-vertical", summary="Run vertical OCR on an image.")
async def route_tesseract_jpn_vertical(image: bytes = File()):
    return pytesseract.image_to_string(
        image=Image.open(io.BytesIO(image)),
        lang="jpn_vert",
    )
