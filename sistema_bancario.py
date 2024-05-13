lass ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios < 3 and valor <= 500:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_diarios += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Erro: Saldo insuficiente para realizar o saque.")
        else:
            print("Erro: Limite diário de saques atingido ou valor de saque excede R$ 500.00.")

    def extrato(self):
        print("Extrato:")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f" - R$ {deposito:.2f}")
        print("Saques:")
        for saque in self.saques:
            print(f" - R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Função principal para interação com o usuário
def main():
    conta = ContaBancaria()

    while True:
        print("\n1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
