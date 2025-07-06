@echo off
title Gerenciador do Servidor Flask - Sistema de Reserva de Salas

:menu
cls
echo ========================================
echo    GERENCIADOR DO SERVIDOR FLASK
echo ========================================
echo.
echo [1] Iniciar servidor
echo [2] Parar servidor
echo [3] Verificar status
echo [4] Instalar dependencias
echo [5] Sair
echo.
set /p opcao="Escolha uma opcao (1-5): "

if "%opcao%"=="1" goto iniciar
if "%opcao%"=="2" goto parar
if "%opcao%"=="3" goto status
if "%opcao%"=="4" goto instalar
if "%opcao%"=="5" goto sair
goto menu

:iniciar
cls
echo ========================================
echo    INICIANDO SERVIDOR
echo ========================================
echo.
call start_server.bat
goto menu

:parar
cls
echo ========================================
echo    PARANDO SERVIDOR
echo ========================================
echo.
call stop_server.bat
goto menu

:status
cls
echo ========================================
echo    STATUS DO SERVIDOR
echo ========================================
echo.
echo Verificando se o servidor esta rodando...
netstat -an | findstr :5000 >nul 2>&1
if errorlevel 1 (
    echo [INFO] Nenhum servidor rodando na porta 5000
) else (
    echo [INFO] Servidor Flask esta rodando na porta 5000
    echo [INFO] Acesse: http://localhost:5000
)

if exist "flask.pid" (
    set /p PID=<flask.pid
    echo [INFO] PID do servidor: %PID%
) else (
    echo [INFO] Arquivo flask.pid nao encontrado
)
echo.
pause
goto menu

:instalar
cls
echo ========================================
echo    INSTALANDO DEPENDENCIAS
echo ========================================
echo.
echo [INFO] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado! Instale o Python primeiro.
    pause
    goto menu
)

echo [INFO] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Erro ao instalar dependencias!
) else (
    echo [SUCESSO] Dependencias instaladas com sucesso!
)
echo.
pause
goto menu

:sair
cls
echo ========================================
echo    SAINDO DO GERENCIADOR
echo ========================================
echo.
echo Obrigado por usar o Sistema de Reserva de Salas!
echo.
exit /b 0 