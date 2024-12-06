@echo off
echo Setting up SSL certificates...

REM Get your domain
set /p DOMAIN="Enter your domain (e.g., your-domain.com): "
set /p EMAIL="Enter your email: "

REM Get certificate
certbot certonly --standalone -d %DOMAIN% --email %EMAIL% --agree-tos --non-interactive

echo SSL setup complete!
pause 