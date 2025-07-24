from datetime import datetime
import textwrap


def menu():
    menu = """
    ======================================
    Bem-vindo ao Sistema Bancário V1
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    -> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"[{timestamp}] Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.") 
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    if valor <= 0:
        print("Valor inválido. Tente novamente...")
        return saldo, extrato, numero_saques

    elif numero_saques >= LIMITE_SAQUES:
        print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques). ")
        return saldo, extrato, numero_saques

    elif valor > saldo:
        print("Saldo insuficiente para saque.")
        return saldo, extrato, numero_saques

    elif valor > limite:
        print(f"Valor do saque excede limite de R$ {limite:.2f}. ")
        return saldo, extrato, numero_saques

    else:
        saldo -= valor
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f'[{timestamp}] Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n============= Extrato =============")
    if not extrato:
        print("Nenhuma transação feita.")
    else:
        print(extrato.strip())
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=================================\n")

def criar_usuario(usuarios):

    cpf = (input("Digite seu CPF: (sem pontos e/ou traços).").strip())
    usuario = filtrar_usuarios(cpf, usuarios)
    

    if not cpf:
        print("CPF não pode ser vazio... Tente novamente")
        return

    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Digite exatamente os 11 números.")
        return

    if filtrar_usuarios(cpf, usuarios):
        print("Já existe um usuário com esse CPF!")
        return
        
    nome = input("Digite seu nome completo: ").strip()

    if not nome:
        print("Nome não pode ser vazio... Tente novamente")
        return

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

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o seu CPF (somente números): ").strip()
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")
    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

if __name__ == "__main__":
    main()
