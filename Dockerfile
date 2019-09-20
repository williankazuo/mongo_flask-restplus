FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get install -y python3-pip python3-dev build-essential

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt


