FROM python:3.10-buster-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN pip install poetry

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml /app/
COPY poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app/
ENTRYPOINT ./run.sh