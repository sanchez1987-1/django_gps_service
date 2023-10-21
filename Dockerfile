# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/
COPY gps_service/ /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
EXPOSE 8008
