def CadastrarTarefa(tarefas, titulo, descricao, prioridade, classe_tarefa):
    nova_tarefa = classe_tarefa(titulo, descricao, prioridade)
    tarefas.append(nova_tarefa)
    return nova_tarefa

def ListarTarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(
            f"\nId: {i}"
            f"\nTítulo: {tarefa.titulo}"
            f"\nDescrição: {tarefa.descricao}"
            f"\nPrioridade: {tarefa.prioridade}"
            f"\nSituação: {tarefa.situacao}"
            f"\n------------------------------"
        )

def FiltrarPorSituacao(tarefas, situacao):
    tarefas_filtradas = []

    for tarefa in tarefas:
        if tarefa.situacao == situacao:
            tarefas_filtradas.append(tarefa)

    return tarefas_filtradas

def LerDadosTarefa():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade: ")

    return titulo, descricao, prioridade
