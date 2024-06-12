class ContaBancaria:
  def __init__(self, numero_conta, titular, saldo):
      self.numero_conta = numero_conta
      self.titular = titular
      self.saldo = saldo

  def verificar_saldo(self):
      return self.saldo

  def deposito(self, deposito):
      self.saldo += deposito

  def sacar(self, saque):
      self.saldo -= saque
