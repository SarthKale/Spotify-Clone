#!/bin/bash

set -e

python manage.py migrate
python manage.py runserver

exit 0
