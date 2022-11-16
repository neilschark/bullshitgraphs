FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN pip install poetry

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml /app/
COPY poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --only main

COPY run_prod.sh /app
COPY flask-app /app/flask-app
COPY bullshitgraphs /app/bullshitgraphs

ENTRYPOINT ./run_prod.sh
