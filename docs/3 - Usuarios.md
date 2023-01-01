# Usuarios
Os usuarios podem ser encontrados na pasta [users/](../users/). Cada subpasta representa um usuario em que o nome da pasta é o _nome do usuario_.
## Tipo de usuario
### Comum
O usuario comum tem permissões limitadas o que inclui:
1. Criar uma conta;
2. Deletar a sua conta;
3. Gerenciar a sua coleção (adcionar e remover jogos);
4. Favoritar jogos;
5. Privar os seus jogos aos outros utilizadores comuns;
6. Ver e favoritar jogos publicos;
7. Criar listas de jogos.
### Administrador
O administrador tem todas as permissões e é possivel ter varios administradores basta que o atributo _admininstrador_ seja _True_ no arquivo de configruação do usuario.
## Arquivo de configuração
O arquivo de configuração _.config_ contem os dados referentes ao usuario.
- Nome de usuario;
- Nome;
- Palavrapasse;
- Admininstador;
```
username="usertest"
name="user test"
palavrapasse="1234"
administrador=False
```
## Coleção
Sempre que um usuario cria um jogo permanece na sua coleção e só desaparece que quando é deletado.
A coleção pretence a um usuario e só ele e o administrador conseguem o ver. A coleção são um conjunto de jogos que o utulizador criou, jogos que o 'pertencem'. Somente o utilizador e o administrador tem a permissão de remover, adcionar ou editar jogos dessa lista.
A coleção é um arquivo com a extensão .txt (_collection.txt_) em que o id dos jogos são separados por ponto e virgulas.
```1;2;4;5;6;9```
O jogo arquivo do jogo tambem contem um atributo ```username``` que diz qual foi o usuario que criou o jogo.
## Favoritos
Diferente da [coleção](#Coleção), o favorito é uma lista que os artigos devem ser explicitamente adcionados que podem ser jogos criados pelo usuario ou qualquer jogo publico. Os favoritos tambem é uma lista pessoal que só pode ser acessado pelo usuario ou administrador.
O arquivo de favoritos segue a mesma _fashion_ que o de coleção com o nome de _favoritos.txt_.
## Listas
É possivel criar lista de jogos da mesma forma que ser criam pastas no seu computador. Criar uma lista e depois podes adcionar qualquer jogo acessivel (jogos publicos ou criados pelo usuario).
As listas ficam guardas no arquivo _list.config_ em que cada nome de lista é um _key_ e os seus jogos são o seu _value_ numa forma de lista separado por virgulas.
```
Relax="1;2;3;7"
Jogar com amigos="2;3;4;2;2"
```
## Temas
É possivel criar um tema customizado para o programa com um arquivo _theme.config_ na pasta do usuario. O arquivo deve ter alguns atributos que são as cores a serem usadas.
```
PRINCIPAL="#242526"
SECUNDARIA="#6D7073"
ESCURO="#293540"
CLARO="#4B5F73"
BRANCO="#B6BABF"
```
Cada cor subscreve as cores padrões e caso o atributo não existe o programa usa o tributo do global.
## Organização de pastas
Sendo o usuario _UserTest1_:
```
users/
|--- UserTest1/
	|--- .config
	|--- collection.txt
	|--- favorites.txt
	|--- list.config
	|--- theme.config
```

