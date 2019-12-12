FROM python:3.8-alpine
MAINTAINER Sajeesh
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip install -r ./requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app/ /app
# RUN addUser -D user
# USER user