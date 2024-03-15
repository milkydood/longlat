#!/bin/sh

source /app/env/bin/activate
exec python3 /app/longlat.py "$@"
