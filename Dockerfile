# syntax=docker/dockerfile:1
FROM python:3.11
RUN apt-get update && apt-get install -y libpython3.11-minimal libpython3.11-stdlib
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/
COPY gps_service/ /app/
RUN pip install -r /app/requirements.txt
WORKDIR /app
RUN python manage.py collectstatic --noinput
EXPOSE 8008
CMD ["uwsgi", "--ini", "uwsgi.ini"]

