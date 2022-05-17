FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

WORKDIR /app/backend

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]