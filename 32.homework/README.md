Запуск контейнера:

# docker-compose up --build -d

Запуск тестов:

# docker-compose run app python -m unittest discover -v

Просмотр логов:

# docker-compose logs -f app

Остановка контейнера:

# docker-compose down

Запуск Jenkins:

# docker compose -f jenkins-docker-compose.yml up --build -d

Отключить контейнер:

# docker compose -f jenkins-docker-compose.yml down

# http://localhost:8080

# cat /Users/$(whoami)/.jenkins/secrets/initialAdminPassword