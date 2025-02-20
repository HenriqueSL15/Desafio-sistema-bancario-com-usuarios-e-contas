# 1- Separar todo o código em funções: sacar, depositar, visualizar extrato

# 2 - Criar 2 funções, uma para criar um cliente e a outra para criar uma conta corrente e vincular com o cliente

# Função saque = keyword only
# Função deposito = positional only
# Função extrato = positional only e keyword only (argumentos nomeados: saldo / argumentos posicionais: extrato)

# Ao criar o usuário, algumas regras devem ser seguidas:
# os usuários devem ser armazenados em uma lista
# 1 usuário é composto por nome, data de nascimento, cpf e endereço
# o endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado
# Deve ser armazenado somentes os números do CPF.
# Não podemos cadastrar mais de 1 usuário com o mesmo CPF

# Ao criar uma conta corrente, algumas regras devem ser seguidas:
# As contas devem ser armazenadas em uma lista
# 1 conta corrente é composta por: agência, número da conta e usuário	
# O número da conta é sequencial, iniciando em 1
# A agência é fixa: "0001"
# Não podemos cadastrar mais de 1 conta com o mesmo número de conta e mesma agência
# O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

# Dica
# Para vincular um usuário a uma conta, filtre a lista de usuários
# buscando o número de CPF informado para cada usuário da
# lista.

menu = """

[nu] Criar usuário
[nc] Criar conta
[lc] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

AGENCIA = "0001"
numero_da_conta = 1

usuarios = []
contas = []

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    print("Saque realizado com sucesso! \n")
    return saldo, extrato, numero_saques
    

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    
    else:
        print("Operação falhou! O valor informado é inválido.")
    print("Depósito realizado com sucesso! \n")
    return saldo, extrato
    

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def listar_contas(cpf):
    for conta in contas:
        if conta["usuario"] == cpf:
            usuario = filtrar_usuario(cpf)
            print("*" * 100)
            print("Conta: ", conta["numero_conta"])
            print("Agência: ", conta["agencia"])
            print("Usuário: ", usuario["nome"])
            print("*" * 100)
    print("Todas as contas foram exibidas!")
        
        

def filtrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe usuário com esse CPF!")
            return
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    return

def criar_conta(numero_conta, usuario, agencia=AGENCIA,):
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print("\nConta criada com sucesso!")
    

while True:

    opcao = input(menu)

    if opcao == "nu":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        criar_usuario(nome, data_nascimento, cpf, endereco)
    elif opcao == "nc":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)

        if usuario:
            criar_conta(numero_conta=numero_da_conta, usuario=usuario["cpf"])
            numero_da_conta+=1
        else:
            print("Usuário não encontrado, fluxo de criação de conta encerrado!")
    elif opcao == "d":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)

        if usuario:
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "lc":
        usuario = input("Informe o CPF do usuário: ")
        existe_usuario = filtrar_usuario(usuario)

        if existe_usuario:
            print("\nConta(s) do usuário:")
            listar_contas(usuario)
    elif opcao == "s":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf)

        if usuario:
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")