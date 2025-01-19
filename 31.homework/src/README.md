Запуск контейнера:

# docker-compose up --build -d

Запуск тестов:

# docker-compose run app python -m unittest discover -v

Просмотр логов:

# docker-compose logs -f app