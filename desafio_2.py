import textwrap

def menu():
    menu = """\n
    -------- MENU --------

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [NC] Nova Conta
    [LC] Lista Contas
    [NU] Novo Usuario
    [S] Sair

    """
    return input(menu)

def depositar(saldo, valor, extrato, /):# / Recebe argumentos por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito Realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido")
    
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):# recebe argumentos apenas por nome
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
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):# saldo/ Recebe argumentos por posição e # * extrato Recebe argumento por nome
    print("\n _____Extrato____")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("___________________")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (Somente números):" )
    usuario: filtrar_usuario(cpf, usuarios)

    if usuarios: #Se já existe usuário cadastrato informe, se não Return para cadastro
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("Usuário criado com sucesso!!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None # 0 Retorna o primeiro elemento pois não pode cadastrar dois usuários com o mesmo CPF, se não encontrar retona None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF (Somente números)" )
    usuarios: filtrar_usuario(cpf, usuarios)

    if usuarios: 
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}
    print("Usuário não encontrado, fluxo de conta encerrado") #Quando não retona nada na função é exatamente como a linha return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuarios']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    saldo = 5000
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 4
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("\n Informe o valor do depósito"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao =="S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)
    
        elif opcao =="NC":
            numero_conta = len(contas) +1 #tamanho da minha lista conta + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(contas)
        
        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")                   
main()