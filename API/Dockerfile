FROM python:3.8-slim

WORKDIR /API

COPY ./API ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD uvicorn main:app --port 8080 --host 0.0.0.0
