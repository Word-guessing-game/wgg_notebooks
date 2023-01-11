#!/usr/bin/env bash

echo "Запуск тестов"

MONGO_USER_NAME=admin \
  MONGO_USER_PASSWORD=123 \
  MONGO_DATABASE_NAME=test_db \
  MONGO_HOST=127.0.0.1 \
  pytest .
