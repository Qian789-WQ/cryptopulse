#!/bin/bash
# Render 启动脚本
exec gunicorn cryptopulse.api.app:app --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120
