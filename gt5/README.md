# GT5 source code

Aqui contem tudo o 'kernel' do programa. O arquivo principal é o [app.py](app.py) que é o arquivo que deves executar no terminal.

## Organização de pastas

Mesmo o [app.py](app.py) sendo o arquivo principal, o ponto de entrada ele não contem nenhum codigo muito relevante ele só executa codigo em outro arquivos que estes sim contem coisas relevantes.

### [lib/](lib/)

Contem as routinas mais genericas coisas como: autenticação de usuario, temas, utilitarios genericos, etc.

### [pages/](pages/)

Contem as declarações de classes que montam as diferentes paginas do app.

### [widgets/](widgets/)

Contem as classes que definem os diferentes wigets do app.

## Discleimer

Ao executar o app deves estar no root do projeto (pasta principal do projeto não nas subpastas) pois a app usa caminho relativos ao root do projeto e caso seja executado dentro de uma subpasta o caminho passa a ser relativo a subpasta.
O root do projeto é o [repositorio](https://github.com/rocha1202/TrabalhoPratico_AED/) contendo este projecto.

Tambem é importante que o ambiente virtual esteja ativado.