chamados = [
{"id": 1,
"titulo": "Sem acesso ao sistema interno",
"prioridade": "alta",
"situacao": "aberto",
"categoria": "acesso"},
{"id": 2,
"titulo": "Impressora sem conexão",
"prioridade": "média",
"situacao": "em atendimento",
"categoria": "hardware"},

{"id": 3,
"titulo": "Internet caindo com frequência",
"prioridade": "alta",
"situacao": "em atendimento",
"categoria": "acesso"},
{"id": 4,
"titulo": "Wi-fi com baixo alcance",
"prioridade": "média",
"situacao": "aberto",
"categoria": "hardware"},
{"id": 5,
"titulo": "Mouses com defeito",
"prioridade": "alta",
"situacao": "aberto",
"categoria": "hardware"}
]

def ListarChamados():
    for i in chamados:
        print(f"\nId: {i["id"]}\nTítulo: {i["titulo"]}\nPrioridade: {i["prioridade"]}\nSituação: {i["situacao"]}\nCategoria: {i["categoria"]}\n------------------------------")
    return

def FiltrarChamados():
    print("Situações: 1 - aberto | 2 - em atendimento | 3 - concluído | 4 - cancelado")
    escolha = input("Informe qual situação você está procurando: ")
    if escolha == "1":
        escolha = "aberto"
    elif escolha == "2":
        escolha = "em atendimento"
    elif escolha == "3":
        escolha = "concluído"
    elif escolha == "4":
        escolha = "cancelado"
    else:
        return print("Opção inválida! Retornando ao menu...")
    for i in chamados:
        if escolha == i["situacao"]:
            print(f"\nId: {i["id"]}\nTítulo: {i["titulo"]}\nPrioridade: {i["prioridade"]}\nSituação: {i["situacao"]}\nCategoria: {i["categoria"]}\n------------------------------")
    if any(escolha in i["situacao"] for i in chamados) == False: # ou: if not any(escolha == i["situacao"] for i in chamados):
            return print("Não foi encontrado nenhum chamado com essa situação. Retornando ao menu...")
    return

def AtualizarChamados():
    escolha = int(input("Informe o Id do chamado que deseja atualizar: "))
    for i in chamados:
        if escolha == i["id"]:
            i["situacao"] = "concluído"
            return print(f"Chamado '{i["titulo"]}' teve sua situação atualizada para concluída.")
    else:
        return print("Id não encontrado. Retornando ao menu...")

def CategoriasSemRepeticao():
    lista = []
    for i in chamados:
        lista.append(i["categoria"])
    listaS = set(lista)
    print("Categorias de chamados: ")
    for l in listaS:
        print(l)
    return

def Menu():

    while True:
        print("\n                                          Gerenciador de chamados internos                                          \n" \
              "1 - Listar Chamados | 2 - Filtrar Chamados | 3 - Atualizar Chamados | 4 - Todas as Categorias | 5 - Fechar Gerenciador\n")
        escolha = input("O que deseja fazer: ")

        if escolha == "1":
            ListarChamados()

        elif escolha == "2":
            FiltrarChamados()

        elif escolha == "3":
            AtualizarChamados()

        elif escolha == "4":
            CategoriasSemRepeticao()

        elif escolha == "5":
            return print("Fechando gerenciador...")

        else:
            print("Não entendi sua escolha. Tente novamente.")

Menu()
