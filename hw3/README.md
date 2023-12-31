# Summarizer

Сервис предназначен для сокращения исходного текста

## Пример использования

Запрос:

```shell
curl --location 'http://127.0.0.1:8000/summarize' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Пеле — единственный футболист в мире, три раза становившийся чемпионом мира как игрок (в 1958, 1962 и 1970 годах). Участник четырёх чемпионатов мира. Лучший игрок чемпионата мира 1970. Лучший молодой игрок чемпионата мира 1958. Футболист года в Южной Америке 1973 года. Дважды член символических сборных чемпионатов мира. Двукратный обладатель Межконтинентального кубка и Кубка Либертадорес, победитель Суперкубка межконтинентальных чемпионов, десятикратный чемпион штата Сан-Паулу, четырёхкратный победитель турнира Рио-Сан-Паулу в составе «Сантоса»"
}'
```

Ответ:

```json
{
  "text": "Пеле — единственный футболист в мире, три раза становившийся чемпионом мира как игрок (в 1958, 1962 и 1970 годах). Двукратный обладатель Межконтинентального кубка и Кубка Либертадорес, победитель Суперкубка межконтинентальных чемпионов, десятикратный чемпион штата Сан-Паулу."
}
```

## Установка зависимостей

Для управления зависимостями используется [Poetry](https://python-poetry.org/)

Чтобы установить все зависимости, необходимо выполнить команду

```shell
poetry install
```

Предварительно требуется установить Poetry

---

Так же зависимости указаны в файле [requirements.txt](requirements.txt)

Для установки можно использовать команду:

```shell
pip install -r requirements.txt
```

## Запуск

```shell
uvicorn main:app
```
