import multiprocessing
import time

def tarefa_1():
    print("Processo 1: Contando até 3")
    for i in range(1, 4):
        print(i)
        time.sleep(1)

def tarefa_2():
    print("Processo 2: Exibindo mensagens")
    for _ in range(3):
        print("Executando tarefa 2")
        time.sleep(2)

def tarefa_3():
    print("Processo 3: Somando valores")
    soma = sum(range(1, 6))
    print(f"Resultado da soma: {soma}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=tarefa_1)
    p2 = multiprocessing.Process(target=tarefa_2)
    p3 = multiprocessing.Process(target=tarefa_3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
