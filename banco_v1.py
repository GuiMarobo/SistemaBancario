from datetime import datetime

#positional only
def deposit(saldo, extrato, /):
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
def withdraw(*, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
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
    print("\n============= Extrato =============")
    if not extrato:
        print("Nenhuma transação feita.")
    else:
        print(extrato.strip())
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=================================\n")

def create_user(users):

    user_cpf = (input("Digite seu CPF: (sem pontos e/ou traços).").strip())
    # cpf vazio
    if not user_cpf:
        print("CPF não pode ser vazio... Tente novamente")
        return
    # cpf precisa ter 11 digitos
    if not user_cpf.isdigit() or len(user_cpf) != 11:
        print("CPF inválido. Digite exatamente os 11 números.")
        return
    # cpf não pode estar cadastrado
    for user in users:
        if user["cpf"] == user_cpf:
            print(f"O CPF: [{user_cpf}] já está cadastrado!")
            return
        
    nome = input("Digite seu nome completo: ").strip()
    # nome vazio
    if not nome:
        print("Nome não pode ser vazio... Tente novamente")
        return
    # nome sem sobrenome (se for nome composto passa)
    if len(nome.split()) < 2:
        print("Digite o nome completo: (nome e sobrenome).")
        return
    
    data_nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ").strip()
    if not data_nascimento:
        print("Data de Nascimento não pode ser vazio... Tente novamente")
        return
    if len(data_nascimento) != 10 or data_nascimento[2] != '/' or data_nascimento[5] != '/':
        print("Use o formato dd/mm/aaaa.")
        return
    
    logradouro = input("Logradouro: ").strip()
    if not logradouro:
        print("Logradouro não pode ser vazio...")
        return
    
    numero = input("Número da residência: ").strip()
    if not numero:
        print("Número não pode ser vazio...")
        return
    
    bairro = input("Bairro: ").strip()
    if not bairro:
        print("Bairro não pode ser vazio...")
        return
    
    cidade = input("Cidade: ").strip()
    if not cidade:
        print("Cidade não pode ser vazio...")
        return
    
    uf = input("Estado: ").strip()
    if not uf or len(uf) != 2:
        print("UF inválido. Digite apenas a sigla do estado com 2 letras, ex: SP, RJ, PR.")
        return

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{uf}"

    new_user = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": user_cpf,
        "endereco": endereco
    }

    users.append(new_user)
    print("Usuário cadastrado com sucesso!")

# def create_account():


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
        saldo, extrato = deposit(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = withdraw(
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