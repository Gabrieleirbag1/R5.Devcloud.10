FROM python:3.12-slim

WORKDIR /app
EXPOSE 8000
COPY terrien/ .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
