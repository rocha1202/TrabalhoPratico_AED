# GT5 - Gestor de jogos
![GT5 logo](./img/assets/gt5/banner-gt5.svg)

---

O GT5 é um gestor de jogos bem simples que está sendo desenvolvido como um projeto escolar para a disciplina de **Algoritmia e Estrutura de Dados** para o **[Instituto Pólitécnico do Porto](https://www.ipp.pt/)**.

## Recursos
### Gerenciamento de usuarios
O GT5 é capaz de gerenciar varias contas numa unica instalação.
Para criar uma conta clica no icone no canto inferior esquerdo. A clicar um popup será aberto pedindo o login.
![Login Screenshot](./img/screenshots/login.png)
Podes fazer login como usuario _admin_ com a palavra-passe padrão de **1234** caso seja uma instalação limpa do programa ou podes criar uma nova conta clicando em criar nova conta.
![Criar Conta Screenshot](./img/screenshots/criar_conta.png)
Ao criar uma conta por padrão o usuario não tem nenhuma permissão especial (como criar novas categorias).

### Gerenciamento de jogos
O proposito doo GT5 de gerenciar os seus jogos, para isso basta criar uma conta e clicar no _simbolo de mais_ no canto inferior direito para adcionar os seus jogos.
![jogos](./img/screenshots/jogos.png)
Depois de adcionado o jogo já aparece na sua biblioteca e podes eventualmente deletar, comentar e adcionar aos favoritos.
![Colecção de jogos](./img/screenshots/collection.png)
![Favoritos](./img/screenshots/favoritos.png)

### Comunidade
Caso outro usuario tenha adcionado um jogo previamente podes simplesmente adcionar este as suas lista ou favoritos ao inves de ter que fazer todo o processo de criar o jogo.

## Dependencias
Para usar o programa é necessario ter o python na versão [3.10](https://www.python.org/downloads/release/python-3109/), apos isso use o script [build.sh](build.sh) para fazer o resto da instalação.

- python==3.10
- customtkinter==5.0.3
- darkdetect==0.8.0
- Pillow==9.3.0

### script
O script cria um ambiente virtual, o ativa e usa o requirements.txt para instalar a dependencias e executa o programa.

## Estado
Este programa ainda está em desenvolvento. 

## Utilização
### Linux e Mac
Clone o repositorio:
```
$ git clone https://github.com/rocha1202/TrabalhoPratico_AED

$ cd TrabalhoPratico_AED
```
Execute no seu terminal o script _build.sh_:
```
$ chmod +x build.sh

$ ./build.sh
```

### Windows
Primeiro baixe o linux, depois instale-o e execute os passo acima :).
Brincadeiras a parte, o script para windows será provido em breve.

---
**Tecnologias e Sistemas de Informação para Web**
![Logo TSIW](./img/assets/tsiw/white.svg)