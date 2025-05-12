FROM python:3.11-slim

WORKDIR /app

COPY Boliche.py .

CMD ["python", "Boliche.py"]