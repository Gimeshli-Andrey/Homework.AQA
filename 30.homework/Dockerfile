FROM python:3.9-slim

# Установка зависимостей для проекта
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка Java (для Allure) и Node.js
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl gnupg2 lsb-release && \
    apt-get install -y nodejs npm && \
    npm install -g allure-commandline && \
    apt-get clean

# Установка JAVA_HOME и добавление пути Allure в PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Копирование всех файлов проекта
COPY . .

# Команда по умолчанию
CMD ["pytest", "--alluredir=allure-results", "--disable-warnings"]