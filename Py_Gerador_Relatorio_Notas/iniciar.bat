@echo off

REM Obtém o caminho do diretório onde o arquivo .bat está localizado
for %%i in (%0) do set "bat_dir=%%~dpi"

REM Navega para o diretório onde o arquivo app.py está localizado
cd /d "%bat_dir%"

REM Executa o servidor Flask usando py.exe (ou python.exe, dependendo da sua instalação)
start py.exe app.py

REM Aguarda 2 segundos
ping -n 2 127.0.0.1 > nul

REM Abre o navegador padrão e acessa http://127.0.0.1:5000
start http://127.0.0.1:5000