# Приложение

## Запуск в докер-контейнере:

Сервисы и части приложения можно запускать по отдельности, в разных терминалах:


* Запуск API:
```bash
docker-compose up api
```

* Запуск Клиентской части:
```bash
docker-compose up frontend
```

* Запуск mongodb:
```bash
docker-compose up mongo
```

* Запуск nginx:
```bash
docker-compose up nginx
```

* Так же можно комбинировать, например:
```bash
docker-compose up api mongo
```

* Или запустить всё сразу:
```bash
docker-compose up
```
