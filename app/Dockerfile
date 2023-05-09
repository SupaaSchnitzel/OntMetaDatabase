FROM python:latest

WORKDIR /app

COPY requirements.txt /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5000


ENTRYPOINT flask run --host=0.0.0.0