#!/usr/bin/bash

source .venv/bin/activate

uv pip install -r requirements.txt

gunicorn -c gunicorn_config.py run:app --reload --daemon
