#!/bin/bash

set -e

echo "Configurando ambiente..."

python3 -m venv .venv

echo "Ativando ambiente..."

source .venv/bin/activate

echo "Instalando dependências..."

pip install --upgrade pip

echo "Ambiente virtual pronto!"
