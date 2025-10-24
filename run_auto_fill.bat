@echo off
echo ========================================
echo UAZapigo Multi-Atendimento
echo Preenchimento Automático com Selenium
echo ========================================
echo.

echo Verificando se Python está instalado...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python não está instalado ou não está no PATH
    echo Por favor, instale Python 3.7+ e tente novamente
    pause
    exit /b 1
)

echo Python encontrado!
echo.

echo Instalando dependências...
pip install -r requirements.txt

echo.
echo Executando preenchimento automático...
echo.

python selenium_auto_fill_improved.py

echo.
echo Processo concluído!
pause
