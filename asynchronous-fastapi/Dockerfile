# base image
FROM python:3.10.5-slim-buster

# add a work directory
WORKDIR /asynchronous-fastapi



RUN pip install --upgrade pip
COPY ./requirements.txt /asynchronous-fastapi
RUN pip install --no-cache-dir -r requirements.txt

COPY . /asynchronous-fastapi

CMD ["uvicorn", "app.fastapi_server:app", "--host", "0.0.0.0", "--port", "8001"]