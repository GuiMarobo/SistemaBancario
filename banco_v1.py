from datetime import datetime
#positional only
def depositar(saldo, extrato, /):
    valor = float(input("Digite o valor a ser depositado: R$ "))
    if valor > 0:
        saldo += valor
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"[{timestamp}] Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
            print("Valor inválido. Tente novamente...") 
    return saldo, extrato


#keyword only
def sacar(*, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Digite o valor a ser sacado: R$ "))

    if valor <= 0:
        print("Valor inválido. Tente novamente...")

    elif numero_saques >= LIMITE_SAQUES:
        print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques). ")

    elif valor > saldo:
        print("Saldo insuficiente para saque.")

    elif valor > limite:
        print(f"Valor do saque excede limite de R$ {limite:.2f}. ")

    else:
        saldo -= valor
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f'[{timestamp}] Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques

#positional only e keyword only (positional: saldo keyword: extrato.)
def view_extrato(saldo, /, *, extrato):
    print("\n============ Extrato ============")
    if not extrato:
        print("Nenhuma transação feita.")
    else:
        print(extrato.strip())
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================================\n")


# =================== MENU ===================

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
    
    opcao = input(menu).lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            limite=limite,
            extrato=extrato,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )

    elif opcao == "e":
        view_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Finalizando sistema...")
        break

    else:
        print("Opção inválida, por favor tente novamente.")