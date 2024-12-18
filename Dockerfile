FROM python:3.12.7
LABEL authors="agrytsai"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser --disabled-password --no-create-home st_user

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN mkdir -p /home/st_user/.cache && chown -R st_user:st_user /home/st_user/.cache

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . .

USER st_user

EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
