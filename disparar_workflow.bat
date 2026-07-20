@echo off
title Disparando Workflow do Dashboard no GitHub...
echo ========================================================
echo Disparando Run Workflow (update_data.yml) no GitHub...
echo ========================================================

cd /d "%~dp0"

set GITHUB_TOKEN=

gh workflow run update_data.yml --repo Grupo-FAPES/drhoje-dashboard-ceo

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo SUCESSO! Workflow disparado com sucesso no GitHub!
    echo O robô do GitHub está processando os dados e atualizará
    echo o dashboard em alguns segundos.
    echo ========================================================
    echo.
    echo Aguardando 45 segundos para baixar o resultado...
    timeout /t 45
    git pull
) else (
    echo.
    echo ========================================================
    echo Para autorizar o envio pela primeira vez, execute no terminal:
    echo gh auth login
    echo ========================================================
)

timeout /t 5
