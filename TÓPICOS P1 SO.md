### **📌 TÓPICOS PARA ESTUDAR 📚**  

### **1️⃣ Introdução aos Sistemas Operacionais**  
🔹 O que é um Sistema Operacional (SO)  
🔹 Funções principais do SO  
🔹 Importância do SO na interação entre hardware e software  

### **2️⃣ Arquitetura de Sistemas Operacionais**  
🔹 Relação entre SO e Arquitetura de Computadores  
🔹 Gerenciamento de recursos (CPU, memória, dispositivos de E/S)  
🔹 Modos de operação (usuário e kernel)  

### **3️⃣ Processos e Gerenciamento de Processos**  
🔹 O que é um processo e como ele funciona  
🔹 Diferença entre **processo** e **programa**  
🔹 Estados de um processo (Novo, Pronto, Em Execução, Bloqueado, Finalizado)  
🔹 Ciclo de vida dos processos  

### **4️⃣ Escalonamento de Processos**  
🔹 O que é um escalonador e sua função no SO  
🔹 Tipos de escalonadores (curto, médio e longo prazo)  
🔹 Algoritmos de escalonamento:  
✅ FIFO (First In, First Out)  
✅ LIFO (Last In, First Out)  
✅ SJF (Shortest Job First)  
✅ Prioridade  

Além dos algoritmos básicos mencionados no seu exercício (**FIFO, LIFO, SJF e Prioridade**), existem outros **algoritmos de escalonamento** importantes que podem aparecer na prova. Aqui estão os principais:  

---

### **📌 ALGORTIMOS DE ESCALONAMENTO PARA ESTUDAR**  

### **📍 1. Escalonamento Não-Preemptivo** (O processo executa até terminar)  
✅ **FIFO (First In, First Out)** – O primeiro processo que chega é executado primeiro.  
✅ **LIFO (Last In, First Out)** – O último processo que chega é executado primeiro.  
✅ **SJF (Shortest Job First)** – O processo mais curto é executado primeiro.  
✅ **Prioridade Estática** – O processo com maior prioridade é executado primeiro.  

---

### **📍 2. Escalonamento Preemptivo** (O processo pode ser interrompido antes de terminar)  
🔹 **Round Robin (RR)** – Cada processo recebe um **quantum de tempo** para executar. Se não terminar, volta para o final da fila. **Usado em sistemas multitarefa.**  
🔹 **SRTF (Shortest Remaining Time First)** – Versão preemptiva do SJF. Se um novo processo menor chegar, o atual é interrompido.  
🔹 **Prioridade Dinâmica** – A prioridade dos processos **muda com o tempo**, evitando que processos de baixa prioridade fiquem esperando indefinidamente.  
🔹 **Escalonamento Multinível** – Processos são divididos em **filas diferentes** (ex: interativos x em lote), e cada fila tem regras próprias.  
🔹 **Escalonamento Multinível com Realimentação** – Igual ao anterior, mas um processo pode mudar de fila **com base no seu comportamento**.  

---

### **📍 3. Algoritmos Mais Avançados (Menos Comuns em Provas)**  
🔸 **Escalonamento por Loteria (Lottery Scheduling)** – Cada processo recebe **bilhetes de loteria** e o escalonador escolhe aleatoriamente.  
🔸 **Fair Share Scheduling** – Os processos são escalonados para garantir que **todos os usuários recebam um tempo de CPU justo**.  

---

### **📌 QUAL DELES ESTUDAR MAIS?**  
🔹 **Se a prova for básica:** Priorize **FIFO, LIFO, SJF, Prioridade e Round Robin.**  
🔹 **Se for mais avançada:** Revise também **SRTF, Multinível e Prioridade Dinâmica.**  
🔹 **Se quiser um diferencial:** Dê uma olhada em **Loteria e Fair Share Scheduling.**  

---

### **5️⃣ Multiprogramação e Concorrência**  
🔹 O que é multiprogramação e como melhora o desempenho do SO  
🔹 Diferença entre **multiprogramação** e **multitarefa**  
🔹 Conceito de concorrência e compartilhamento de recursos  
🔹 Problemas da concorrência (ex: deadlock)  

### **6️⃣ Compartilhamento de Recursos e Sincronização**  
🔹 O que é compartilhamento de recursos e sua importância  
🔹 Gerenciamento da CPU, memória e dispositivos entre processos  
🔹 Como evitar monopólio de recursos  

---

### **🎯 DICAS PARA A PROVA**  
✅ **Revise os conceitos teóricos** e entenda **os termos técnicos** usados nas perguntas.  
✅ **Pratique a resolução de códigos**, especialmente **Python com multiprocessing e escalonamento**.  
✅ **Dê exemplos reais** de processos e escalonadores para facilitar a memorização.  
✅ **Revise as relações entre os tópicos**, como **ciclo de vida dos processos, escalonamento e compartilhamento de recursos**.  