import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [pf]\tConta Pessoa Física
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def criar_conta_fisica(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "dependentes": []}

    print("\nUsuário não encontrado. Redirecionando para o cadastro de titular de pessoa física.")
    nome_completo = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço completo: ")

    usuario = {"nome_completo": nome_completo, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}

    dependentes = criar_dependentes(usuario)
    usuario["dependentes"] = dependentes

    usuarios.append(usuario)
    print("\n=== Usuário e dependentes cadastrados com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "dependentes": dependentes}


def criar_dependentes(conta):
    dependentes = []
    while True:
        opcao_dependente = input("\nDeseja cadastrar um dependente? (s/n): ").lower()

        if opcao_dependente != "s":
            break

        nome_completo = input("Informe o nome completo do dependente: ")
        cpf_dependente = input("Informe o CPF do dependente: ")
        data_nascimento_dependente = input("Informe a data de nascimento do dependente (dd/mm/aaaa): ")
        endereco_dependente = input("Informe o endereço completo do dependente: ")

        dependente = {
            "nome_completo": nome_completo,
            "cpf": cpf_dependente,
            "data_nascimento": data_nascimento_dependente,
            "endereco": endereco_dependente,
        }

        dependentes.append(dependente)

    return dependentes





def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
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
    buscar_conta_por_id = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "pf":
            numero_conta = len(contas) + 1
            conta = criar_conta_fisica(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "dep":
            listar_contas(contas)
            conta_id = int(input("\nInforme o ID da conta na qual deseja adicionar dependentes: "))

            conta = buscar_conta_por_id(conta_id, contas)
            if conta is None:
                print("\n@@@ Conta não encontrada. @@@")
            else:
                criar_dependentes(conta)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()