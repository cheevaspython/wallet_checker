
# Микросервис для работы с кошельками Tron



### Для запуска системы выполните команду:

```
docker-compose up -d --build
```


Это поднимет базу данных и сам микросервис. 

## Доступ к Swagger

После того как система будет запущена, вы можете получить доступ к Swagger UI, который предоставляет удобный интерфейс для работы с API:

**Swagger UI** - [http://localhost/docs](http://localhost/docs)

С помощью Swagger UI вы сможете:

- Просматривать доступные эндпоинты.
- Отправлять запросы к API.
- Смотреть документацию по параметрам и ответам.

## Структура проекта

- `docker-compose.yml` — файл конфигурации для запуска всех сервисов (Kafka, база данных, микросервис).
- `source/` — основной код микросервиса.
- `swagger/` — документация для взаимодействия с API.

## Пример использования API

Пример POST-запроса для отправки заявки:

```bash
curl -X 'POST' \
  'http://127.0.0.1/api/v1/wallet/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'value=TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA'

Ответ:

{
  "address": "TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA",
  "free_bandwidth": "600",
  "total_bandwidth": "1000",
  "total_energy": "500",
  "balance": "5168.92",
  "created_date": "01/22/2025, 15:25:43"
}

GET-запрос для получения списка последних запросов:

curl -X 'GET' \
  'http://127.0.0.1/api/v1/wallet/?offset=0&limit=10' \
  -H 'accept: application/json'

Ответ:

{
  "count": 11,
  "results": [
    {
      "id": 1,
      "address": "TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA",
      "free_bandwidth": "600",
      "total_bandwidth": "1000",
      "total_energy": "500",
      "balance": "5168.92",
      "created_date": "01/22/2025, 15:25:43"
    },
    ...
  ]
}
```

Автор: [@nvim_msk]



