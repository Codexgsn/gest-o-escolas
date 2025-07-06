@echo off
echo ========================================
echo    CONFIGURADOR DO SISTEMA ADMIN
echo ========================================
echo.

echo Instalando dependencias...
pip install Flask==3.0.0 Flask-Login==0.6.3 Flask-SQLAlchemy==3.1.1 Werkzeug==3.0.1 SQLAlchemy==2.0.23

echo.
echo Iniciando o sistema...
echo O usuario admin sera criado automaticamente na primeira execucao.
echo.
echo Credenciais do Admin:
echo Email: admin@gmail.com
echo Senha: @dm1n
echo.
echo Pressione qualquer tecla para iniciar o servidor...
pause >nul

python app.py 