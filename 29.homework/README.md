Запуск контейнера:

# bashCopydocker-compose up --build

Запуск тестов:

# bashCopydocker-compose run app python -m unittest discover -v

Просмотр логов:

# bashCopydocker-compose logs -f app