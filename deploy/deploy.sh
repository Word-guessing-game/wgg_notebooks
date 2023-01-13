#!/usr/bin/env bash

echo 'Deploy to server'
echo " - Deployed branch: $(git branch --show-current)"
export APP_PATH="/home/deploy/wgg-app"

rsync -e "ssh -o StrictHostKeyChecking=no" \
      --progress -azhr \
      --exclude ".git/*" \
      --exclude "frontend/node_modules/*" \
      --exclude "frontend/.env" \
      --exclude ".env" \
      . deploy@$HOST:$APP_PATH

ssh deploy@$HOST "\
  cp $APP_PATH/shared/frontend/.env $APP_PATH/frontend_app \
  && cp $APP_PATH/shared/api/.env $APP_PATH \
  && cp $APP_PATH/shared/mongo/password $APP_PATH/deploy/mongo \
  && cp $APP_PATH/shared/mongo/root_password $APP_PATH/deploy/mongo \
  && cd $APP_PATH \
  && docker-compose build \
  && docker-compose up -d \
  && docker system prune --force"

echo "Деплой завершён, приложение доступно по ссылке: http://$HOST:3000"
