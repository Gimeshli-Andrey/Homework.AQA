FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копирование requirements.txt для установки зависимостей
COPY requirements.txt .

# Установка pip и зависимостей
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

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

# Копирование всех файлов проекта в контейнер
COPY . .

# Команда по умолчанию для запуска тестов
CMD ["python3", "-m", "pytest", "--alluredir=allure-results", "--disable-warnings"]