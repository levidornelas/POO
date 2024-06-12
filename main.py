import banco

while True:
    try:
        numero_conta = int(input('Insira o número da sua conta: '))
        titular = input('Insira o nome do titular da conta: ')

        conta = banco.ContaBancaria(numero_conta, titular, 0)
        saldo_atual = conta.verificar_saldo()

        escolhas = ['depositar', 'sacar', 'verificar saldo', 'sair']

        escolha = input(f'Olá, {titular}, seu saldo atual é {saldo_atual}, o que você deseja fazer? ')

        if escolha not in escolhas:
            print('Por favor, escolha uma operação válida.')
            continue

        if escolha == 'verificar saldo':
            print(f'Seu saldo agora é: {saldo_atual}')

        elif escolha.lower() == 'depositar':
            deposito = int(input('Quantos reais você deseja depositar? '))
            conta.deposito(deposito)
            print(f'Depois do depósito, seu saldo é: {conta.verificar_saldo()}')

        elif escolha.lower() == 'sacar':
            saque = int(input(f'Seu saldo agora é {saldo_atual}, Quantos reais você deseja sacar? '))
            saldo_saque = conta.sacar(saque)
            print(f'Depois do saque, seu saldo é: {conta.verificar_saldo()}')

        elif escolha.lower() == 'sair':
            print('Obrigado por utilizar nosso banco! ')
            break

    except ValueError:
        print('O número da conta precisa ser inteiro.')
