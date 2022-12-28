# automatiza o processo de rodar o programa no seu computador
# instalando as dependencias para o programa
# mas ainda é necessario ter o python 3.10 instalado no seu dispossitivo

# cria o ambiente virtual
python3.10 -m venv .venv

# usa o ambiente virtual criado (não sei se funciona no windows)
# (provavelmente não)
source .venv/bin/activate

# instala as dependencias (conecção com a internet necessaria)
python -m pip install -r requirements.txt

# por fim roda o programa
python src/app.py
