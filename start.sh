#!/bin/bash

source /var/www/montecatiniterme.ivirgilius.com/private/django/env/bin/activate
/var/www/montecatiniterme.ivirgilius.com/private/django/manage.py run_gunicorn 0.0.0.0:9066
