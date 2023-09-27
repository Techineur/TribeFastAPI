FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN ls -al

RUN pip install -r requirements.txt

COPY ./app /app

