import banco

print('INSTRUÇÕES AO USUÁRIO:')
print("DIGITE '1' PARA VERIFICAR SALDO'")
print("DIGITE '2' PARA DEPOSITAR")
print("DIGITE '3' PARA SACAR")
print("DIGITE '4' PARA CONFERIR UMA CONTA.")
print("DIGITE '5' PARA CADASTRAR OUTRA CONTA.")
print("DIGITE '6' PARA TRANSFERIR")
print("DIGITE '7' PARA APAGAR UMA CONTA")

# Dicionário para armazenar as contas bancárias
contas = {}

while True:
    try:
        opcoes = [1, 2, 3, 4, 5, 6,7]

        print('OLÁ! Vamos iniciar o processo de criação de conta. Responda ao formulário abaixo:')
        numero_conta = int(input('Insira o número da conta: '))

        if numero_conta in contas:
            print('Já há uma conta com este número. Por favor, insira um número de conta diferente.')
            continue

        titular = input('Digite o nome do titular: ')
        saldo = float(input('Insira o saldo da conta: '))

        conta = banco.ContaBancaria(titular, saldo)
        contas[numero_conta] = conta  

        while True:
            opcao = int(input('O que deseja fazer? '))

            if opcao not in opcoes:
                print('Por favor, escolha uma operação válida.')
                continue

            if opcao == 1:
                print(f'O saldo atual é: {conta.verificar_saldo()}')

            elif opcao == 2:
                deposito = float(input('Digite o valor a ser depositado: '))
                conta.depositar(deposito)
                print(f'O saldo atual é: {conta.verificar_saldo()}')

            elif opcao == 3:
                saque = float(input('Digite o valor a ser sacado: '))
                if saque > conta.verificar_saldo():
                    raise ValueError("Você não tem saldo suficiente para essa transferência.")
                conta.sacar(saque)
                print(f'Seu saldo após o saque realizado é: {conta.verificar_saldo()}')

            elif opcao == 4:
                # Acessando uma conta já cadastrada
                numero_conta_acesso = int(input('Digite o número da conta que deseja acessar: '))
                conta_acesso = contas.get(numero_conta_acesso)

                if conta_acesso:
                    print(f"Titular da conta: {conta_acesso.titular}")
                    print(f"Saldo da conta: {conta_acesso.verificar_saldo()}")
                else:
                    print("Conta não encontrada.")

            if opcao == 5:
                break

            if opcao == 6:
                numero_conta_origem = int(input('Digite o número da conta de origem: '))
                conta_origem = contas.get(numero_conta_origem)
                numero_conta_destino = int(input('Digite o número da conta de destino: '))
                conta_destino = contas.get(numero_conta_destino)

                if conta_origem and conta_destino:
                    valor_transferencia = float(input('Digite o valor a ser transferido: '))
                    conta_origem.transferir(conta_destino, valor_transferencia)

                else:
                    print("Conta de origem ou conta de destino não encontrada.")

            if opcao == 7:
                numero_conta_excluida = int(input('Insira o número da conta que será excluída:'))
                if numero_conta_excluida not in contas:
                    print('A conta não foi encontrada.')
                else:
                    print(f'O {numero_conta_excluida} foi excluído!')
                    del[numero_conta_excluida]


    except ValueError:
        print('Ocorreu um erro')
