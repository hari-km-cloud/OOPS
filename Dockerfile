FROM python:2.7-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app/main.py"]
