FROM python:3.7-slim

WORKDIR /app

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt