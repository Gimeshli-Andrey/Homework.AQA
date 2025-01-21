FROM python:3.9-slim

# Установка зависимостей для проекта
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
# Указываем команду для запуска тестов
CMD ["pytest", "--alluredir=allure-results", "tests/test_registration.py"]
=======
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

# Команда по умолчанию
CMD ["pytest", "--alluredir=allure-results", "--disable-warnings"]
>>>>>>> 65c7bce (Temporary commit to save changes)
