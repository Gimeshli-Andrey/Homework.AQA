# Используем базовый образ Python 3.9
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копирование только requirements.txt для установки зависимостей
COPY requirements.txt .

# Установка pip и зависимостей из requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# Копирование всех остальных файлов проекта
COPY . .

# Установка Java (для Allure) и Node.js
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl gnupg2 lsb-release && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g allure-commandline && \
    apt-get clean

# Установка переменной окружения для JAVA_HOME и добавление в PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Проверка версий Python и Node.js
RUN python3 --version
RUN node --version

# Команда по умолчанию для запуска тестов
ENTRYPOINT ["python3", "-m", "pytest"]
CMD ["--alluredir=allure-results", "--disable-warnings"]
