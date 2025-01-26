Запуск тестов:

# pytest tests/test_app.py --alluredir=allure-results

Просмотр логов:

# allure serve allure-results

Запуск Jenkins:

# docker compose -f jenkins-docker-compose.yml up --build -d

Ключ:

# docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

Логи:

# docker logs jenkins


Отключить контейнер:

# docker compose -f jenkins-docker-compose.yml down



# http://localhost:8080


# ngrok http 8080
