def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (apenas números): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    # Verificar se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def criar_conta_corrente(contas, usuarios):
    cpf = input("Digite o CPF do usuário: ")

    # Verificar se o usuário existe
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Erro: Usuário não encontrado.")
        return

    numero_conta = len(contas) + 1
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    print("Conta corrente criada com sucesso.")
    print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Erro: O valor do depósito deve ser positivo.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques and valor <= limite:
        if saldo >= valor:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Saldo insuficiente para realizar o saque.")
    else:
        print("Erro: Limite diário de saques atingido ou valor de saque excede R$ 500.00.")
    return saldo, extrato

def extrato(saldo, *, extrato):
    print("Extrato:")
    for operacao in extrato:
        print(f" - {operacao}")
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função principal para interação com o usuário
def main():
    usuarios = []
    contas = []

    while True:
        print("\n1. Cadastrar usuário")
        print("2. Cadastrar conta corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario(usuarios)
        elif opcao == '2':
            criar_conta_corrente(contas, usuarios)
        elif opcao == '3':
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
            if conta:
                valor = float(input("Digite o valor a ser depositado: "))
                conta['saldo'], conta['extrato'] = depositar(conta.get('saldo', 0), valor, conta.get('extrato', []))
            else:
                print("Conta não encontrada.")
        elif opcao == '4':
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
            if conta:
                valor = float(input("Digite o valor a ser sacado: "))
                conta['saldo'], conta['extrato'] = sacar(
                    saldo=conta.get('saldo', 0),
                    valor=valor,
                    extrato=conta.get('extrato', []),
                    limite=500,
                    numero_saques=conta.get('numero_saques', 0),
                    limite_saques=3
                )
            else:
                print("Conta não encontrada.")
        elif opcao == '5':
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
            if conta:
                extrato(conta.get('saldo', 0), extrato=conta.get('extrato', []))
            else:
                print("Conta não encontrada.")
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
