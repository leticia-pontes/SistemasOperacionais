"""
LETÍCIA ALVES DE PONTES - 1979942
"""

import time

# Funções que simulam os processos
def processo_p1():
    print("Executando o processo P1")
    time.sleep(1)

def processo_p2():
    print("Executando o processo P2")
    time.sleep(1)

def processo_p3():
    print("Executando o processo P3")
    time.sleep(1)

def processo_p4():
    print("Executando o processo P4")
    time.sleep(1)


# First In, First Out
def fifo(processos):
    # Ordena pelo tempo de chegada
    for _, _, _, _, func in sorted(processos, key=lambda x: x[0]):
        func()

# Shortest Job First
def sjf(processos):
    # Ordena pelo tempo de chegada e pela menor duração
    for _, _, _, _, func in sorted(processos, key=lambda x: (x[0], x[1])):
        func()

# Round Robin
def round_robin(processos, quantum=1):
    processos_restantes = processos[:]
    while processos_restantes:
        processo = processos_restantes.pop(0)
        tempo_restante = processo[1]
        tempo_executado = min(quantum, tempo_restante)
        print(f"Executando o processo {"P" + processo[4].__name__[-1]} por {tempo_executado} unidades de tempo")
        time.sleep(tempo_executado)
        tempo_restante -= tempo_executado
        if tempo_restante > 0:
            processos_restantes.append((processo[0], tempo_restante, processo[2], processo[3], processo[4]))

# Prioridade
def prioridade(processos):
    # Ordena por prioridade, tempo de chegada e tamanho. Executa os de maior prioridade primeiro
    for _, _, _, _, func in sorted(processos, key=lambda x: (-x[3], x[0], x[2])):
        func()

# Last In, First Out
def lifo(processos):
    # Ordena pelo tempo de chegada e pela menor duração. Executa a partir do último a chegar
    for _, _, _, _, func in sorted(processos, key=lambda x: (-x[0], x[1])):
        func()


if __name__ == "__main__":
    # Lista de processos (tempo de chegada, duração, tamanho*, prioridade, função correspondente)
    processos = [
        (0, 5, 26, 1, processo_p1),
        (0, 3, 30, 3, processo_p2),
        (0, 1, 21, 1, processo_p3),
        (0, 1, 15, 5, processo_p4)
    ]

    print("Executando FIFO: ")
    fifo(processos)
    print("Executando SJF: ")
    sjf(processos)
    print("Executando Round Robin: ")
    round_robin(processos)
    print("Executando Prioridade: ")
    prioridade(processos)
    print("Executando LIFO: ")
    lifo(processos)