#!/usr/bin/env bash

echo "Старт API"
cd ./api

MONGO_USER_NAME=admin \
  MONGO_USER_PASSWORD=123 \
  MONGO_DATABASE_NAME=development_db \
  MONGO_HOST=127.0.0.1 \
  uvicorn app.main:app --reload
