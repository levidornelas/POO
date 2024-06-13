class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def verificar_saldo(self):
        return self.saldo

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        self.saldo -= saque

    def transferir(self, conta_destino, valor):
        if valor > self.saldo:
            raise ValueError("Você não tem saldo suficiente para essa transferência.")
            
        self.sacar(valor)
        conta_destino.depositar(valor)
        
        print(f'Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.titular}.')
        print(f'Seu saldo atual é: R${self.verificar_saldo():.2f}')
