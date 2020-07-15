#!/bin/bash
pytest -v --tb=short -p no:warnings -m sanity1 --arg StLukes | tee Logs/log_file.log
python notification.py