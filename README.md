# Gerenciador de Chamados Internos - gerenciador_chamados.py

# Tarefa realizada pelo trio:
## * João Victor Barboza Debossan - Nº de Matrícula: 202422915
## * Lucas Malfacine Rodrigues    - Nº de Matrícula: 202422972
## * Lucca de Andrade Vianna Braz - Nº de Matrícula: 202422924


## Objetivo do Programa

O programa **gerenciador_chamados.py** foi desenvolvido em Python com o objetivo de armazenar 
chamados em forma de dicionários que oferecem operações básicas de gerenciamento de suporte técnico.

O sistema disponibiliza funções para:

- Listar todos os chamados cadastrados;
- Filtrar chamados de acordo com sua situação;
- Atualizar a situação de um chamado para **concluído**;
- Exibir as categorias de chamados sem repetição;
- Encerrar o programa por meio do menu principal.


## Comando para Execução

Para executar o programa, é necessário ter o **Python 3** instalado.
No terminal, navegue até a pasta onde o arquivo está salvo e execute:

* bash
python nome_do_arquivo.py

Por exemplo, caso o arquivo se chame `chamados.py`:

* bash
python chamados.py


## Exemplo de Uso

Ao iniciar o programa, será apresentado o menu principal:

* Gerenciador de chamados internos

1 - Listar Chamados     | 
2 - Filtrar Chamados    | 
3 - Atualizar Chamados  | 
4 - Todas as Categorias | 
5 - Fechar Gerenciador

O que deseja fazer:


### Listar chamados
Ao selecionar a opção `1`, o programa apresenta os chamados cadastrados:

Id: 1
Título: Sem acesso ao sistema interno
Prioridade: alta
Situação: aberto
Categoria: acesso
------------------------------

Id: 2
Título: Impressora sem conexão
Prioridade: média
Situação: em atendimento
Categoria: hardware
------------------------------


### Filtrar chamados
Selecionando a opção `2`, o programa permite escolher uma situação:

* Situações: 1 - aberto | 2 - em atendimento | 3 - concluído | 4 - cancelado
Informe qual situação você está procurando: 1

O sistema então apresenta somente os chamados que possuem a situação escolhida.


### Atualizar chamado
Na opção `3`, é possível informar o ID de um chamado:

* Informe o Id do chamado que deseja atualizar: 1
Chamado 'Sem acesso ao sistema interno' teve sua situação atualizada para concluída.


### Consultar categorias
A opção `4` apresenta as categorias cadastradas sem repetições:

* Categorias de chamados:
acesso
hardware


### Encerrar o programa
Ao selecionar `5`:

* Fechando gerenciador...
