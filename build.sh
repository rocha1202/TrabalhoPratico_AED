# cria o ambiente virtual
python3 -m venv .venv

# usa o ambiente virtual criado
source .venv/bin/activate

# instala as dependencias (conecção com a internet necessaria)
pip install -r requirements.txt

# por fim roda o programa
python main.py