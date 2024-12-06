@echo off
echo Starting SecureAuth in development mode...

REM Activate virtual environment
call venv\Scripts\activate

REM Set Flask environment variables
set FLASK_APP=web/security_monitor.py
set FLASK_ENV=development
set FLASK_DEBUG=1

REM Start Flask development server
python -m flask run --host=127.0.0.1 --port=5000

pause 