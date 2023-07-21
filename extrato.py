# A função verificar_saldo é definida com dois parâmetros: saldo e valor.
def verificar_saldo(saldo, valor):
    """
    Verifica se o saldo está positivo antes de realizar uma operação.

    Args:
        saldo: O saldo atual da conta.
        valor: O valor da operação.

    Returns:
        True se o saldo for positivo, False caso contrário.
    """
    if saldo < 0:
        print("O saldo está negativo.")
        return False
    return True

# Esta linha define a função mostrar_saldo com um parâmetro saldo, que representa o saldo atual da conta.
def mostrar_saldo(saldo):
    """
    Exibe o saldo disponível.

    Args:
        saldo: O saldo atual da conta.
    """
    print(f"Saldo disponível: R$ {saldo:.2f}")

# A variável menu é definida como uma string delimitada por três aspas triplas """,
# o que permite que a string abranja várias linhas
menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[t] Transferência Bancária
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

# Exibindo o saldo inicial
mostrar_saldo(saldo)


# Criando um loop infinito com while True no bloco de operação até que uma condição de saída seja alcançada 
# ou o loop seja interrompido explicitamente com uma instrução de break.
while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")
            continue

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            mostrar_saldo(saldo)
        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")
            continue

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(
                f"Você ainda pode fazer {LIMITES_SAQUES - numero_saques} saques.")
            mostrar_saldo(saldo)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Nenhuma movimentação registrada no extrato." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    elif opcao == "t":
        try:
            nome_completo = input("Informe o nome completo (até 50 caracteres): ")
            # A função len() é uma função embutida do Python que retorna o tamanho (ou o comprimento) de um 
            # objeto, como uma string, lista, tupla, etc.
            if len(nome_completo) > 50:
                print("Erro de digitação! O nome completo deve ter até 50 caracteres.")
                continue

            numero_agencia = input(
                "Informe o número da agência bancária (até 4 dígitos): ")
            
            #isdigit() é usado para verificar se a entrada do usuário (por exemplo, número da agência, código, 
            # número da conta, código verificador) contém apenas dígitos numéricos. Caso contrário, uma mensagem 
            # de erro é exibida para indicar que o usuário digitou um valor inválido.
            if not numero_agencia.isdigit() or len(numero_agencia) > 4:
                print("Erro de digitação! O número da agência deve conter até 4 dígitos numéricos.")
                continue

            codigo = input(
                "Informe o código (13 para poupança ou 25 para conta corrente, até 2 dígitos): ")
            if not codigo.isdigit() or len(codigo) > 2:
                print("Erro de digitação! O código deve conter até 2 dígitos numéricos.")
                continue

            numero_conta = input("Informe o número da conta (até 6 dígitos): ")
            if not numero_conta.isdigit() or len(numero_conta) > 6:
                print("Erro de digitação! O número da conta deve conter até 6 dígitos numéricos.")
                continue

            codigo_verificador = input("Informe o código verificador (até 1 dígito): ")
            if not codigo_verificador.isdigit() or len(codigo_verificador) > 1:
                print("Erro de digitação! O código verificador deve conter até 1 dígito numérico.")
                continue

            valor_transferencia = float(
                input("Informe o valor da transferência (até R$ 1000): "))
            if valor_transferencia > 1000:
                print("Valor máximo permitido para transferência é de R$ 1000.")
                continue
        except ValueError:
            print("Valor inválido! Por favor, insira um valor permitido.")
            continue
        # criada uma mensagem de transferência bancária com informações fornecidas pelo usuário. O texto é 
        # formatado usando uma f-string, que é uma maneira conveniente de inserir variáveis e expressões em 
        # uma string    
        transferencia_bancaria = f"Nome completo: {nome_completo}\nNúmero da agência bancária: {numero_agencia}\nCódigo: {codigo}\nNúmero da conta: {numero_conta}\nCódigo verificador: {codigo_verificador}\nValor da transferência: R$ {valor_transferencia:.2f}"
        print(transferencia_bancaria)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    