#!/bin/bash
pytest -v --tb=short -p no:warnings -m sanity --arg $1 | tee Logs/log_file.log
python notification.py $1
