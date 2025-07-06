@echo off
echo ========================================
echo    SISTEMA DE RESERVA DE SALAS
echo ========================================
echo.

REM Verifica se já existe um processo rodando
if exist "flask.pid" (
    echo [AVISO] Encontrado arquivo flask.pid. Removendo...
    del flask.pid
)

REM Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado! Instale o Python primeiro.
    pause
    exit /b 1
)

REM Verifica se as dependências estão instaladas
echo [INFO] Verificando dependencias...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo [INFO] Instalando dependencias...
    pip install -r requirements.txt
)

REM Inicia o servidor Flask
echo [INFO] Iniciando servidor Flask...
echo [INFO] O servidor estara disponivel em: http://localhost:5000
echo [INFO] Para parar o servidor, pressione Ctrl+C
echo.
echo ========================================
echo.

python app.py

REM Se chegou aqui, o servidor foi parado
if exist "flask.pid" (
    del flask.pid
)
echo.
echo [INFO] Servidor parado.
pause 