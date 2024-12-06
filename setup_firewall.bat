@echo off
echo Setting up Windows Firewall rules...

REM Add firewall rules for HTTP and HTTPS
netsh advfirewall firewall add rule name="SecureAuth HTTP" dir=in action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="SecureAuth HTTPS" dir=in action=allow protocol=TCP localport=443
netsh advfirewall firewall add rule name="SecureAuth Gunicorn" dir=in action=allow protocol=TCP localport=5000

echo Firewall rules added!
pause 