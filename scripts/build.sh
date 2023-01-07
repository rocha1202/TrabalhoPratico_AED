# automatiza o processo de rodar o programa no seu computador
# instalando as dependencias para o programa
# mas ainda é necessario ter o python 3.10 instalado no seu dispossitivo

# testa se o ambiente virtual existe
ls .venv/

# caso o ambiente virtual ainda não exista vamos criar
if [[ $(echo $?) != 0 ]]; then
  echo Criando o ambiente virtual na pasta .venv
  # cria o ambiente virtual
  python3.10 -m venv .venv

  # ativa o ambiente virtual
  source ./scripts/activate.sh

  echo Instalando as dependencias
  # instala as dependencias (conecção com a internet necessaria)
  python -m pip install -r requirements.txt
fi
