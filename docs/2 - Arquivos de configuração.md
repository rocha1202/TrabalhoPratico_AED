# Arquivos de Configuração
Os arquivos de configuração padrão podem ser encontrados na pasta [.config](../.config/). Os arquivos são todos de texto legivel ao ser humano com o enconding UTF-8 no formato _key=value_ que podem ser facilmente editados diretamento ou atraves da interface.
## Extensão
Os arquivos contem todos a extensão _.config_. O arquivo padrão só tem a extensão [.config](../.config/.config).
## Formatação
O tipo de formato escolhido de _key=value_ faz com que seja muito facil manipular os dados no programa e ao mesmo tempo muito eligivel e intuitivo. Tambem é possivel ter uma lista como value basta separa os valores por uma virgual. Tambem é possivel ter comentarios só começar a linha com um hashtag (#) que o programa ignora.
## Arquivos
Na pasta contem alguns arquivos já predefinidos:
- [themes.config](../.config/theme.config): Contem as definições da paleta de cor padrão do app.
- [game.config]: Contem as configurações usadas pelo modulo [game.py](../gt5/lib/game.py) que é o responsavel por criar e gerenciar os jogos. Contem definições como o proximo o id do jogo.
- [.config](../.config/.config): Contem as configurações do app como o nome do app, o admin e o caminho do tema padrão.
## Parser
Para converter o arquivos de configuração para uma estrutura de dados que o python entenda precisamos de um parser. O parser em questão é parte do modulo [utils.py](../gt5/lib/utils.py). Ele converte o texto no ficheiro em questão e retorna um dicionario do python. Durante a conversão o parser passa por 3 fases:
1. Ignora os comentarios;
2. Separa os keys dos values;
3. Faz o tratamento dos values. Convertendo para inteiro ou lista caso seja possivel.
## Deparser
Se o parser converte o texto para python o deparser faz o inverso convertendo o python para texto, repitindo os mesmo passos de traz para frente. O deparser tambem é parte do mesmo modulo implementado como uma função como nome ```make(__filepath, __data)``` que recebe o caminho para o arquivo e os dados num dicionario.
O deparser reescreve o arquivo mas somente os dados contidos no ```__data``` serão reescritos e os comentarios preservados.
## [[3 - Usuarios|Usuarios]]
Os arquivos dos usarios vão para a sua pasta pessoal com nome de .config (ex: users/\<username\>/). O arquivo de configuração que contem os dados do usuario tem o nome de _.config_ assim como o arquivo de configuração global. Os outros arquivos são os arquivos de configuração os de coleção, favoritos e lista.
## [[4 - Jogos | Jogos]]
Os arquivos na pasta games, ou seja os dados dos jogos são todos arquivos de configuração. Os dados do jogo são todos guardados neste arquivo. O nome do arquivo é o ID (_identification number_) do jogo.
O **ID** é um numero inteiro que autoincrimento da mesma forma que acontece numa base de dados relacional (ex: como o _mysql_) o ID do proximo jogo a ser adcionado pode ser encatrado no arquivo de configuração global dos jogos [.config/game.config](../.config/game.config).