@echo off
echo Starting SecureAuth...

REM Activate virtual environment
call venv\Scripts\activate

REM Set Flask environment variables
set FLASK_APP=web/security_monitor.py
set FLASK_ENV=production

REM Start Gunicorn
python -m gunicorn --bind 127.0.0.1:5000 web.wsgi:application

pause 