FROM python:3.10-slim-buster

# Install system dependencies.
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-jpn \
    tesseract-ocr-jpn-vert

# Install dependencies.
RUN pip install --no-cache-dir pdm
ADD ./pyproject.toml ./pdm.lock ./
RUN pdm sync && pdm cache clear

ADD ./main.py ./
CMD pdm run uvicorn --host 0.0.0.0 --port $PORT main:app

