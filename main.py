from tarefa import Tarefa
from servicos import CadastrarTarefa, ListarTarefas, FiltrarPorSituacao

tarefas = []

def CadastrarPeloTerminal():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade: ")

    nova_tarefa = CadastrarTarefa(
        tarefas,
        titulo,
        descricao,
        prioridade,
        Tarefa
    )
    print(f"Tarefa '{nova_tarefa.titulo}' cadastrada com sucesso.")


def FiltrarTarefas():
    print("\nSituações:")
    print("1 - Pendente")
    print("2 - Concluída")

    escolha = input("Informe qual situação você está procurando: ")

    if escolha == "1":
        situacao = "Pendente"
    elif escolha == "2":
        situacao = "Concluída"
    else:
        print("Opção inválida! Retornando ao menu...")
        return

    tarefas_filtradas = FiltrarPorSituacao(tarefas, situacao)

    if not tarefas_filtradas:
        print("Não foi encontrada nenhuma tarefa com essa situação.")
        return

    ListarTarefas(tarefas_filtradas)


def ConcluirTarefa():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    ListarTarefas(tarefas)

    escolha = int(input("Informe o número da tarefa que deseja concluir: "))

    if escolha < 1 or escolha > len(tarefas):
        print("Número de tarefa não encontrado.")
        return

    tarefa = tarefas[escolha - 1]

    if tarefa.situacao == "Concluída":
        print("Essa tarefa já está concluída.")
        return

    tarefa.concluir()

    print(
        f"Tarefa '{tarefa.titulo}' teve sua situação "
        f"atualizada para concluída."
    )


def Menu():
    while True:
        print(
            "\n                 Gerenciador de tarefas internas                 \n"
            "1 - Listar Tarefas / "
            "2 - Filtrar Tarefas / "
            "3 - Concluir Tarefa / "
            "4 - Cadastrar Tarefa / "
            "5 - Fechar Gerenciador\n"
        )

        escolha = input("O que deseja fazer: ")

        if escolha == "1":
            ListarTarefas(tarefas)

        elif escolha == "2":
            FiltrarTarefas()

        elif escolha == "3":
            ConcluirTarefa()

        elif escolha == "4":
            CadastrarPeloTerminal()

        elif escolha == "5":
            print("Fechando gerenciador...")
            return

        else:
            print("Não entendi sua escolha. Tente novamente.")


# Demonstração solicitada pela atividade
CadastrarTarefa(
    tarefas,
    "Sem acesso ao sistema interno",
    "Verificar o acesso do funcionário ao sistema interno",
    "Alta",
    Tarefa
)

CadastrarTarefa(
    tarefas,
    "Impressora sem conexão",
    "Verificar a conexão da impressora",
    "Média",
    Tarefa
)

CadastrarTarefa(
    tarefas,
    "Internet caindo com frequência",
    "Verificar problemas na conexão da internet",
    "Alta",
    Tarefa
)

# Demonstração da mudança de estado
tarefas[0].concluir()

print("Todas as tarefas:")
ListarTarefas(tarefas)

print("\nTarefas concluídas:")
tarefas_concluidas = FiltrarPorSituacao(tarefas, "Concluída")
ListarTarefas(tarefas_concluidas)


Menu()
