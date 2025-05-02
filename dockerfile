FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# RUN chmod +x code_coffee.py

CMD ["python", "code_coffee.py"]
