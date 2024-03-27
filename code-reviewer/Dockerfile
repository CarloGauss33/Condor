FROM python:3.8-slim-buster

WORKDIR /app
ADD . /app

RUN apt-get update
RUN pip install -e .
CMD ["review_pull_request"]
