# Деплой приложения

## Зависимости

Для локального развёртывания удобно использовать:

- [Poetry](https://python-poetry.org/)
- утилиту [Make](https://ru.wikipedia.org/wiki/Make)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Сборка и запуск

Для поднятия всех сервисов в Docker достаточно выполнить команду

```shell
make up
```

Чтобы остановить работу сервисов, есть команда

```shell
make down
```
