FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "--alluredir=allure-results", "tests/test_registration.py"]