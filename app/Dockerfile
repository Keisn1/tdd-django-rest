ARG PYTHON_VERSION
FROM python:3.11.5-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY ./pyproject.toml .
RUN poetry install

COPY . .
    MAINTAINER  <kay@archlinux>
