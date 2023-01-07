# retorna a plataforma onde o programa está a ser executado

# chama o utilitario uname para obter o codinome do sistema operativo
# Linux
# Darwin -> MacOS
# WindowsNT -> Microsoft Windows
# FreeBSD
OS=$(uname)
plataform='unknown'

# detecta a plataforma
case "$OS" in
  'Linux') plataform='Unix';;
  'Darwin') plataform='Unix';;
  'WindowsNT') plataform='Windows';;
  'FreeBSD') plataform='Unix'
esac