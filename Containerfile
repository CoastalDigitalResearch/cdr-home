FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/
COPY content/ ./content/
COPY agents/ ./agents/
COPY blog/ ./blog/

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
