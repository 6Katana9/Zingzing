FROM python:3.12.2-slim

WORKDIR ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
