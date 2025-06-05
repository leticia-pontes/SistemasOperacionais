import multiprocessing

def soma():
    resultado = 5 + 3
    print(f"Soma: 5 + 3 = {resultado}")

def subtracao():
    resultado = 10 - 4
    print(f"Subtração: 10 - 4 = {resultado}")

def saudacao():
    usuario = "João"
    print(f"Hello, {usuario}!")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=soma)
    p2 = multiprocessing.Process(target=subtracao)
    p3 = multiprocessing.Process(target=saudacao)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Todos os processos terminaram.")
