#!/bin/bash
set -a
. /app/.env
set +a
cd app

# Ejecutar comandos de Alembic
PYTHONPATH=/app alembic revision --autogenerate -m "Inicial"
PYTHONPATH=/app alembic upgrade head

# exec uvicorn main:app --host 0.0.0.0 --port 8000
