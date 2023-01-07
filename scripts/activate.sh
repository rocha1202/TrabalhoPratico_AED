# ativa o ambiente virtual do python

# define a plataforma
source ./scripts/plataform.sh

echo Plataforma $plataform detectado

# no linux, mac e freebsd
if [[ "$plataform" == "Unix" ]]; then
  source .venv/bin/activate
elif [[ "$plataform" == "Windows" ]]; then
  # roda no cmd.exe            roda no powershell
    .venv\Script\activate.bat || venv\Scripts\Activate.ps1
fi