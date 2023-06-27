#!/bin/bash

REPOSITORY=/home/ubuntu/EnvEdu_Django
cd $REPOSITORY

touch test

python3 ./manage.py runserver
