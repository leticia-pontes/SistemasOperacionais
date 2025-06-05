import multiprocessing
import threading
import time
import os
import psutil


def memoria_consumida():
    # Obtém informações do processo atual
    processo = psutil.Process(os.getpid())
    # Retorna o uso de memória em KB
    return processo.memory_info().rss / 1024

# Função executada tanto por processos quanto por threads
def tarefa(nome):
    print(f'{nome} iniciado')
    time.sleep(10)
    print(f'{nome} finalizado')

if __name__ == '__main__':
    # Processos
    print('\nIniciando demonstração com PROCESSOS\n')
    memoria_inicio = memoria_consumida()
    inicio = time.time()

    processo1 = multiprocessing.Process(target=tarefa, args=('Processo 1',))
    processo2 = multiprocessing.Process(target=tarefa, args=('Processo 2',))
    processo3 = multiprocessing.Process(target=tarefa, args=('Processo 3',))
    processo4 = multiprocessing.Process(target=tarefa, args=('Processo 4',))
    processo5 = multiprocessing.Process(target=tarefa, args=('Processo 5',))
    processo6 = multiprocessing.Process(target=tarefa, args=('Processo 6',))
    processo7 = multiprocessing.Process(target=tarefa, args=('Processo 7',))
    processo8 = multiprocessing.Process(target=tarefa, args=('Processo 8',))
    processo9 = multiprocessing.Process(target=tarefa, args=('Processo 9',))
    processo10 = multiprocessing.Process(target=tarefa, args=('Processo 10',))
    processo11 = multiprocessing.Process(target=tarefa, args=('Processo 11',))
    processo12 = multiprocessing.Process(target=tarefa, args=('Processo 12',))
    processo13 = multiprocessing.Process(target=tarefa, args=('Processo 13',))
    processo14 = multiprocessing.Process(target=tarefa, args=('Processo 14',))
    processo15 = multiprocessing.Process(target=tarefa, args=('Processo 15',))
    processo16 = multiprocessing.Process(target=tarefa, args=('Processo 16',))
    processo17 = multiprocessing.Process(target=tarefa, args=('Processo 17',))
    processo18 = multiprocessing.Process(target=tarefa, args=('Processo 18',))
    processo19 = multiprocessing.Process(target=tarefa, args=('Processo 19',))
    processo20 = multiprocessing.Process(target=tarefa, args=('Processo 20',))
    processo21 = multiprocessing.Process(target=tarefa, args=('Processo 21',))
    processo22 = multiprocessing.Process(target=tarefa, args=('Processo 22',))
    processo23 = multiprocessing.Process(target=tarefa, args=('Processo 23',))
    processo24 = multiprocessing.Process(target=tarefa, args=('Processo 24',))
    processo25 = multiprocessing.Process(target=tarefa, args=('Processo 25',))

    processo1.start()
    processo2.start()
    processo3.start()
    processo4.start()
    processo5.start()
    processo6.start()
    processo7.start()
    processo8.start()
    processo9.start()
    processo10.start()
    processo11.start()
    processo12.start()
    processo13.start()
    processo14.start()
    processo15.start()
    processo16.start()
    processo17.start()
    processo18.start()
    processo19.start()
    processo20.start()
    processo21.start()
    processo22.start()
    processo23.start()
    processo24.start()
    processo25.start()

    processo1.join()
    processo2.join()
    processo3.join()
    processo4.join()
    processo5.join()
    processo6.join()
    processo7.join()
    processo8.join()
    processo9.join()
    processo10.join()
    processo11.join()
    processo12.join()
    processo13.join()
    processo14.join()
    processo15.join()
    processo16.join()
    processo17.join()
    processo18.join()
    processo19.join()
    processo20.join()
    processo21.join()
    processo22.join()
    processo23.join()
    processo24.join()
    processo25.join()

    tempo_execucao = time.time() - inicio
    memoria_usada = memoria_consumida()
    print(f'\nProcessos finalizados em {tempo_execucao:.2f} segundos')
    print(f'Memória consumida: {(memoria_usada - memoria_inicio):.2f} KB')

    """
    Vantagens e desvantagens de processos:  
    - Vantagens: Melhor isolamento, segurança e aproveitamento de múltiplos núcleos da CPU.  
    - Desvantagens: Maior consumo de memória e tempo de criação/destruição mais longo.  
    """

    # Threads
    print('\nIniciando demonstração com THREADS\n')
    memoria_inicio = memoria_consumida()
    inicio = time.time()

    thread1 = threading.Thread(target=tarefa, args=('Thread 1',))
    thread2 = threading.Thread(target=tarefa, args=('Thread 2',))
    thread3 = threading.Thread(target=tarefa, args=('Thread 3',))
    thread4 = threading.Thread(target=tarefa, args=('Thread 4',))
    thread5 = threading.Thread(target=tarefa, args=('Thread 5',))
    thread6 = threading.Thread(target=tarefa, args=('Thread 6',))
    thread7 = threading.Thread(target=tarefa, args=('Thread 7',))
    thread8 = threading.Thread(target=tarefa, args=('Thread 8',))
    thread9 = threading.Thread(target=tarefa, args=('Thread 9',))
    thread10 = threading.Thread(target=tarefa, args=('Thread 10',))
    thread11 = threading.Thread(target=tarefa, args=('Thread 11',))
    thread12 = threading.Thread(target=tarefa, args=('Thread 12',))
    thread13 = threading.Thread(target=tarefa, args=('Thread 13',))
    thread14 = threading.Thread(target=tarefa, args=('Thread 14',))
    thread15 = threading.Thread(target=tarefa, args=('Thread 15',))
    thread16 = threading.Thread(target=tarefa, args=('Thread 16',))
    thread17 = threading.Thread(target=tarefa, args=('Thread 17',))
    thread18 = threading.Thread(target=tarefa, args=('Thread 18',))
    thread19 = threading.Thread(target=tarefa, args=('Thread 19',))
    thread20 = threading.Thread(target=tarefa, args=('Thread 20',))
    thread21 = threading.Thread(target=tarefa, args=('Thread 21',))
    thread22 = threading.Thread(target=tarefa, args=('Thread 22',))
    thread23 = threading.Thread(target=tarefa, args=('Thread 23',))
    thread24 = threading.Thread(target=tarefa, args=('Thread 24',))
    thread25 = threading.Thread(target=tarefa, args=('Thread 25',))
    
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
    thread17.start()
    thread18.start()
    thread19.start()
    thread20.start()
    thread21.start()
    thread22.start()
    thread23.start()
    thread24.start()
    thread25.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()
    thread13.join()
    thread14.join()
    thread15.join()
    thread16.join()
    thread17.join()
    thread18.join()
    thread19.join()
    thread20.join()
    thread21.join()
    thread22.join()
    thread23.join()
    thread24.join()
    thread25.join()

    tempo_execucao = time.time() - inicio
    memoria_usada = memoria_consumida()
    print(f'\nThreads finalizados em {tempo_execucao:.2f} segundos')
    print(f'Memória consumida: {(memoria_usada - memoria_inicio):.2f} KB')

    """
    Vantagens e desvantagens de threads:  
    - Vantagens: Menor consumo de memória e tempo de criação/destruição menor.  
    - Desvantagens: Menor isolamento (um erro pode afetar outras threads) e maior complexidade de sincronização devido ao compartilhamento de memória.
    """