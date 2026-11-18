#!/bin/sh
set -e
exec gunicorn smsssite.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
