#!/bin/bash

source /opt/config/config.ini

echo "AWS Region: $AWS_REGION"
echo "AWS Account ID: $AWS_ACCOUNT_ID"

# Replace these values with your specific ones
APP_NAME="fastapi_todo"
APP_PATH="/opt/dev_custom/projects/$APP_NAME/"

cd $APP_PATH
cd deploy/prod

#git stash
#git checkout main
#git pull origin main

docker pull $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$APP_NAME:latest

LOG_DIR="/var/dev_data/$APP_NAME/log"
DATA_DIR="/var/dev_data/$APP_NAME"

if [ ! -d $LOG_DIR ]; then
    mkdir -p $LOG_DIR
    chown -R www-data:www-data $LOG_DIR
fi

if [ ! -d $DATA_DIR ]; then
    mkdir -p $DATA_DIR
    chown -R www-data:www-data $DATA_DIR
fi

docker-compose down -v
docker-compose up -d