@echo ir a script

set "RUTAACTUAL=%cd%"
cd\
cd C:\Users\Gonza\AppData\Local\Programs\Python\Python38-32\Scripts
pip install social-auth-app-django
@echo presione enter para volver a la carpeta de proyecto
pause
cd\
cd "%RUTAACTUAL%"
pause