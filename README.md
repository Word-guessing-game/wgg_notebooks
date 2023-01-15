# Приложение
Работающий экземпляр приложения можно открыть по [этой ссылке](http://158.160.24.191:3000).
В первый раз ваш браузер может отобразить предупреждение:
![http warning message](./docs/images/2023-01-15_01-18.png)
Нажмите кнопку "Перейти на сайт". Откроется сайт:
![site screenshot](./docs/images/2023-01-15_01-21.png)

## Запуск в локальном окружении
> Предварительно запустите mongo командой `docker-compose up mongo`

* Запуск API:
```bash
./script/run_api_dev.sh
```

* Запуск Клиентской части:
```bash
./script/run_front_dev.sh
```

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

## Деплой приложения

* С локального компьютера
```bash
./deploy/deploy.sh
```
где HOST - ip адрес или DNS имя хоста, на котором будет запущено приложение.

## Запуск тестов

> Перед запуском тестов нужно запустить mongo, например в контейнере: `docker-compose up -d mongo`

* Тесты можно запускать в докер-контейнере:
```bash
./docker/run_tests.sh
```

* Так же тесты можно запускать в локальном окружении:
```bash
poetry run pytest -v
```
