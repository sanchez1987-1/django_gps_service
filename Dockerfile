# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./gps_service/ /app/
WORKDIR /app
EXPOSE 8008
