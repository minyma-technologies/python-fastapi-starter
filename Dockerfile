FROM python:3.10-slim-buster

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root

CMD poe prod