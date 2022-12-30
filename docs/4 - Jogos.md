# Jogos
Os jogos podem ser encontrados na pasta [games](../games). Cada arquivo é um jogo em que o nome é o [[#ID]] do jogo.
## ID
O ID do jogo é autoincrementado e segue uma ordem natural de adesão. O ID nunca se repete e é unico para cada jogo e mesmo se um jogo for removido o seu ID não é reutilizado para evitar conflitos pois todas as operação com jogo envolvem de alguma forma o uso do seu ID.
Nenum jogo deve ser refenciado por outro atributo que não seja o seu ID.
## Atributos
Dentro do arquivo de configuração contem alguns dados (atributos):
```
nome="Dead Cells"
discription="Jogo rougue-like de ação."
data="07-08-2018"
username="UserTest1"
command="C:\programs\DeadCells\DeadCells.exe"
private=False
tags="violence;rougue-like;rpg"
banner=""
```
- **nome**: O nome do jogo que é obrigatorio;
- **discription**: Uma breve discrição do jogo;
- **data**: Data opcional de lançamento do jogo;
- **username**: O usuario que criou o jogo;
- **command**: Um comando opcional que será executado no terminal ao clicar no play;
- **private**: booleano que diz se o jogo é privado ou não;
- **tags**: uma lista de tags discritivas do jogo
- **banner**: path opcional para o banner do jogo.
Os dados opcionais podem ou não aparecer no arquivo.
## Caso o usuario seja deletado
Caso um usuario seja deletado todos os jogos que ele criou, ou seja, os jogos que tem o atributo _username_ com o nome do usuario são deletados.