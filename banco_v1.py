menu = """
======================================
    Bem-vindo ao Sistema Bancário V1
    [d] Depositar
    [s] Sacar
    [e] Extrato 
    [q] Sair
======================================

Digite a opção desejada:
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        elif valor <= 0:
            print("Valor inválido para depósito. Valor deve ser maior que zero.")
        else:
            print("Valor inválido. Tente novamente...") 

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: R$ "))
        if valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques). ")
        elif valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f}.")


    elif opcao == "e":
        print("=== Extrato ===")
        if not extrato:
            print("Nenhuma transação feita.")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Finalizando sistema...")
        break

    else:
        print("Opção inválida, por favor tente novamente.")