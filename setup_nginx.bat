@echo off
echo Setting up Nginx...

REM Download and extract Nginx
powershell -Command "Invoke-WebRequest -Uri 'http://nginx.org/download/nginx-1.24.0.zip' -OutFile 'nginx.zip'"
powershell -Command "Expand-Archive -Path 'nginx.zip' -DestinationPath 'C:\' -Force"

REM Copy our Nginx config
copy web\nginx\secureauth.conf C:\nginx-1.24.0\conf\

REM Start Nginx
C:\nginx-1.24.0\nginx.exe

echo Nginx setup complete!
pause 