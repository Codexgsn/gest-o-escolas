@echo off
echo ========================================
echo    PARANDO SERVIDOR FLASK
echo ========================================
echo.

REM Verifica se existe arquivo PID
if exist "flask.pid" (
    echo [INFO] Encontrado arquivo flask.pid
    set /p PID=<flask.pid
    echo [INFO] Tentando parar processo PID: %PID%
    
    REM Tenta parar o processo pelo PID
    taskkill /PID %PID% /F >nul 2>&1
    if errorlevel 1 (
        echo [AVISO] Processo %PID% nao encontrado ou ja foi parado
    ) else (
        echo [SUCESSO] Processo %PID% parado com sucesso
    )
    
    REM Remove o arquivo PID
    del flask.pid
    echo [INFO] Arquivo flask.pid removido
) else (
    echo [INFO] Arquivo flask.pid nao encontrado
)

REM Procura por processos Python que possam estar rodando o Flask
echo [INFO] Procurando por processos Python relacionados ao Flask...
for /f "tokens=2" %%i in ('tasklist /FI "IMAGENAME eq python.exe" /FO CSV ^| findstr python.exe') do (
    echo [INFO] Encontrado processo Python: %%i
    echo [INFO] Verificando se e o servidor Flask...
    
    REM Verifica se o processo está usando a porta 5000
    netstat -ano | findstr :5000 | findstr %%i >nul 2>&1
    if not errorlevel 1 (
        echo [INFO] Processo %%i esta usando a porta 5000
        echo [INFO] Parando processo %%i...
        taskkill /PID %%i /F >nul 2>&1
        if not errorlevel 1 (
            echo [SUCESSO] Processo %%i parado com sucesso
        )
    )
)

echo.
echo [INFO] Verificacao final...
netstat -an | findstr :5000 >nul 2>&1
if errorlevel 1 (
    echo [SUCESSO] Nenhum servidor rodando na porta 5000
) else (
    echo [AVISO] Ainda ha um servidor rodando na porta 5000
    echo [INFO] Tente parar manualmente com Ctrl+C no terminal
)

echo.
echo ========================================
echo [INFO] Operacao concluida!
echo ========================================
pause 