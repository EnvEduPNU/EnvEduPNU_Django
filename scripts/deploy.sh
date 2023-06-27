#!/bin/bash

REPOSITORY=/home/ubuntu/EnvEdu_Django
cd $REPOSITORY

RUNNING_NAME='/usr/bin/python3 ./manage.py'

CURRENT_PID=$(pgrep -f $RUNNING_NAME)

if [ -z $CURRENT_PID ]
then
  echo "> 종료할것 없음."
else
  echo "> kill -9 $CURRENT_PID"
  sleep 5
  kill -15 $CURRENT_PID
fi

python3 ./manage.py runserver
