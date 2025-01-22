# Используем базовый образ с Python 3.12
FROM python:3.12-slim

# Установка зависимостей для проекта
WORKDIR /app
COPY requirements.txt .

# Установка зависимостей проекта
RUN pip3 install --no-cache-dir -r requirements.txt

# Установка Java (для Allure) и Node.js
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl gnupg2 lsb-release && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g allure-commandline && \
    apt-get clean

# Установка JAVA_HOME и добавление пути Allure в PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Копирование всех файлов проекта
COPY . .

# Команда по умолчанию для запуска тестов
CMD ["python3", "-m", "pytest", "--alluredir=allure-results", "--disable-warnings"]