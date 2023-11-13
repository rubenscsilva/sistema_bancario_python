menu =  """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''

numero_saque = 0
LIMITE_SAQUES  = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do  deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
        else:
            print('Operação falhou! O valor informado é inválido.')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor >  saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou! Você nã tem saldo suficiente.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor do sque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saque por dia excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print('Operação falhou! O valor informado é inválido.')
    
    elif opcao == 'e':
        print('\n========== Extrato ==========')
        print('Nao foram realizadoas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===============================d')
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')