@echo off
:: Move the command prompt's focus to the folder where this script is
cd /d "%~dp0"
title Future Planner Command Center
echo 🚀 Launching from: %cd%
start http://127.0.0.1:5000
python app.py
pause