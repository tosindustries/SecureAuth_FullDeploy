@echo off
echo Setting up SecureAuth environment...

REM Create virtual environment if it doesn't exist
if not exist venv (
    python -m venv venv
    echo Created virtual environment
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Create .env if it doesn't exist
if not exist .env (
    copy .env.example .env
    echo Created .env file - please update with your settings
)

echo Setup complete!
pause 