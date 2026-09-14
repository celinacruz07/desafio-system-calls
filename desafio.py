import os
import subprocess
import sys


# ==========================================
# 1. CRIAR ARQUIVO
# ==========================================
def operacao1():
    print("\n--- OPERAÇÃO 1: CRIAR ARQUIVO ---")

    nome_arquivo = "exemplo.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("")

    print("Arquivo criado com sucesso!")


# ==========================================
# 2. ESCREVER E LER DADOS
# ==========================================
def operacao2():
    print("\n--- OPERAÇÃO 2: ESCREVER E LER DADOS ---")

    nome_arquivo = "exemplo.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("Sistemas Operacionais\n")
        arquivo.write("Desafio de System Calls na Prática\n")

    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()

    print("\nConteúdo do arquivo:")
    print(conteudo)


# ==========================================
# 3. CRIAR E LISTAR DIRETÓRIO
# ==========================================
def operacao3():
    print("\n--- OPERAÇÃO 3: CRIAR E LISTAR DIRETÓRIO ---")

    nome_diretorio = "meu_diretorio"

    if not os.path.exists(nome_diretorio):
        os.mkdir(nome_diretorio)

    print("Diretório criado com sucesso!")

    print("\nConteúdo do diretório atual:")
    print(os.listdir("."))


# ==========================================
# 4. OBTER O PRÓPRIO PID
# ==========================================
def operacao4():
    print("\n--- OPERAÇÃO 4: OBTER O PRÓPRIO PID ---")

    pid_atual = os.getpid()

    print("PID do processo atual:", pid_atual)


# ==========================================
# 5. CRIAR OUTRO PROCESSO E AGUARDAR
# ==========================================
def operacao5():
    print("\n--- OPERAÇÃO 5: CRIAR PROCESSO E AGUARDAR ---")

    processo = subprocess.Popen(
        [
            sys.executable,
            "-c",
            "import os; import time; "
            "print('PID do processo filho:', os.getpid()); "
            "time.sleep(3); "
            "print('Processo filho finalizando...')"
        ]
    )

    print("\nPID do processo filho:", processo.pid)
    print("Aguardando o processo filho finalizar...")

    processo.wait()

    print("Processo filho finalizado com sucesso!")


# ==========================================
# MENU
# ==========================================
def menu():
    while True:
        print("\n==========================================")
        print("       DESAFIO SYSTEM CALLS")
        print("==========================================")
        print("1 - Criar arquivo")
        print("2 - Escrever e ler dados")
        print("3 - Criar e listar diretório")
        print("4 - Obter próprio PID")
        print("5 - Criar processo e aguardar")
        print("0 - Executar todas as operações")
        print("9 - Sair")
        print("==========================================")

        opcao = input("Digite o número da operação: ")

        if opcao == "1":
            operacao1()

        elif opcao == "2":
            operacao2()

        elif opcao == "3":
            operacao3()

        elif opcao == "4":
            operacao4()

        elif opcao == "5":
            operacao5()

        elif opcao == "0":
            operacao1()
            operacao2()
            operacao3()
            operacao4()
            operacao5()

        elif opcao == "9":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida! Digite um número do menu.")


# ==========================================
# INICIAR PROGRAMA
# ==========================================
menu()