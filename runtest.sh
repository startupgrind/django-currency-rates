#!/bin/sh
if [ -z "$1" ]; then
  MODULES="currency_rates"
else
  MODULES=$1
fi
coverage run --branch --source=currency_rates example/manage.py test $MODULES
coverage report --omit=local_settings.py,settings.py,manage.py,"*/migrations/*.py","*/wsgi.py"
coverage html --omit=local_settings.py,settings.py,manage.py,"*/migrations/*.py","*/wsgi.py"
#coverage xml --omit=local_settings.py,settings.py,manage.py,"*/migrations/*.py","*/wsgi.py"

