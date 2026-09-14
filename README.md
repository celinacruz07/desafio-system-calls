# Desafio System Calls na Prática

Desafio prático da disciplina de Sistemas Operacionais, desenvolvido em Python para demonstrar operações relacionadas aos serviços do sistema operacional.

## Objetivo

Demonstrar, por meio de um programa em Python, diferentes operações que envolvem arquivos, diretórios e processos, compreendendo a relação entre a aplicação, as APIs e os serviços do sistema operacional.

## Operações implementadas

### 1. Criar arquivo
Criação do arquivo `exemplo.txt`.

- Função/API: `open()`
- Modo utilizado: `"w"` (write)
- Serviço do sistema operacional: gerenciamento de arquivos

### 2. Escrever e ler dados
Escrita de informações no arquivo e posterior leitura do seu conteúdo.

- Funções/API: `open()`, `write()` e `read()`
- Serviço do sistema operacional: gerenciamento de arquivos

### 3. Criar e listar diretório
Criação do diretório `meu_diretorio` e listagem do conteúdo do diretório atual.

- Funções/API: `os.mkdir()` e `os.listdir()`
- Serviço do sistema operacional: gerenciamento de diretórios

### 4. Obter o próprio PID
Obtenção do identificador (PID) do processo atual.

- Função/API: `os.getpid()`
- Serviço do sistema operacional: gerenciamento de processos

### 5. Criar outro processo e aguardar
Criação de um processo filho e espera pela finalização de sua execução.

- Funções/API: `subprocess.Popen()` e `processo.wait()`
- Serviço do sistema operacional: gerenciamento de processos

## Tecnologias utilizadas

- Python
- Visual Studio Code
- Git
- GitHub

## Conceito

O projeto demonstra, de forma prática, a relação:

**Aplicação → API → Serviço/System Call → Kernel → Recurso**
