# esse script executa o programa

# faz o build do programa
source ./scripts/build.sh

# ativa o ambiente virtual
source ./scripts/activate.sh

echo Rodando o programa
# Rodar o programa
python ./gt5/app.py