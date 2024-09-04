@echo off
call venv\scripts\activate
pytest -v -s -m "sanity" --html-report=./Reports/report.html --browser chrome
pause