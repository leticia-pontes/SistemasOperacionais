import time
import random
from enum import Enum

# Ciclo de vida de um processo
class ProcessState(Enum):
    NEW = "Novo"
    READY = "Pronto"
    RUNNING = "Executando"
    WAITING = "Esperando"
    TERMINATED = "Finalizado"

class Process:
    def __init__(self, pid, priority): # Inicializa um processo com um ID e prioridade
        self.pid = pid
        self.state = ProcessState.NEW # Define o estado inicial como novo
        self.cpu = None # Inicializa a CPU como None
        self.priority = priority

    def transition(self, used_cpus):
        if self.state == ProcessState.NEW:
            self.state = ProcessState.READY
        
        elif self.state == ProcessState.READY:
            available_cpus = [cpu for cpu in range(1, 1000) if cpu not in used_cpus]
            if available_cpus:
                self.state = ProcessState.RUNNING
                self.cpu = random.choice(available_cpus)
                used_cpus.add(self.cpu)

        elif self.state == ProcessState.RUNNING:
            self.state = random.choice([ProcessState.WAITING, ProcessState.TERMINATED]) # Escolhe aleatoriamente entre "Esperando" e "Finalizado"
            if self.state == ProcessState.TERMINATED or self.state == ProcessState.WAITING:
                used_cpus.discard(self.cpu)
                self.cpu = None

        elif self.state == ProcessState.WAITING:
            self.state = ProcessState.READY

    def __str__(self):
        cpu_info = f" na CPU {self.cpu}" if self.cpu else ""
        return f"Processo {self.pid} (Prioridade {self.priority}): {self.state.value}{cpu_info}"

def main():
    print("\nCICLO DE VIDA DE PROCESSOS\n")

    inicio = time.time()

    processes = [Process(pid, random.randint(1, 10)) for pid in range(1, 2000)]

    while any(p.state != ProcessState.TERMINATED for p in processes):
        processes.sort(key=lambda p: p.priority)
        used_cpus = set()

        for process in processes:
            if process.state != ProcessState.TERMINATED:
                process.transition(used_cpus)
                print(process)
        print("-" * 30)
        time.sleep(1)

    print(f"\nTempo de execução: {(time.time() - inicio):.4f}s")

if __name__ == "__main__":
    main()