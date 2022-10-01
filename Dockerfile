FROM python:3.10-buster

WORKDIR /code

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install poetry
ADD pyproject.toml .
RUN poetry install

