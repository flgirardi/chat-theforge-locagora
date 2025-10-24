#!/bin/bash

echo "========================================"
echo "UAZapigo Multi-Atendimento"
echo "Preenchimento Automático com Selenium"
echo "========================================"
echo

echo "Verificando se Python está instalado..."
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não está instalado"
    echo "Por favor, instale Python 3.7+ e tente novamente"
    exit 1
fi

echo "Python encontrado!"
echo

echo "Instalando dependências..."
pip3 install -r requirements.txt

echo
echo "Executando preenchimento automático..."
echo

python3 selenium_auto_fill_improved.py

echo
echo "Processo concluído!"
