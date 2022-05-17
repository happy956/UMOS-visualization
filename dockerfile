FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

WORKDIR /app/backend

EXPOSE 8080

CMD ["python", "/app/backend/app.py"]