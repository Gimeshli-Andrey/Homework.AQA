FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Установка системных зависимостей, Java, Node.js, и Allure
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jre-headless curl gnupg2 lsb-release && \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    npm install -g allure-commandline && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Установка JAVA_HOME и PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

COPY . .

# Окружение Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

ENTRYPOINT ["pytest"]
CMD ["--alluredir=allure-results", "--disable-warnings"]