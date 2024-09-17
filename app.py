import os
from modulo import * 

if __name__ == '__main__':
    cc = ContaCorrente('','','1001-1','10010-1',0)

    #entrada de dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o CPF do titular: ')

    try:
        while True:
                #saida de dados
            print(f' Nome: {cc.nome}.')
            print(f' CPF: {cc.cpf}.')
            print(f' Agência: {cc.agencia}.')
            print(f' Conta: {cc.conta}.')
            print(f' Saldo: R$ {cc.saldo:,.2f}.\n')

            print('1- Consultar saldo.')
            print('2 - Fazer deposito.')
            print('3 - Fazer saque.')
            print('4 - Sair do programa.')

            opcao = int(input('Informe a opção desejada: '))

            os.system('cls')

            match opcao:
                case 1:
                    print('Consultar saldo\n')
                    print(f'Saldo disponível: R$ {cc.consultar_saldo():,.2f}.')
                    continue

                case 2: 
                    valor = float(input('Informe valor do deposito: R$ ').replace(',','.'))
                    if valor > 0:
                        cc.saldo = cc.fazer_deposito(valor)
                        print('Deposito efetuado com sucesso.')
                    else:
                        print('Valor inválido!')
                    continue
                
                case 3:
                    valor_saque = float(input('Informe valor de saque: R$ '))
                    if valor_saque <= cc.saldo:
                        cc.saldo = cc.fazer_saque(valor)
                        print(f'Saque efetuado com sucesso.')
                    else:
                        print('Não foi possível efetuar o saque.')
                        continue
                case 4:
                    print('Programa encerrado.')
                    break
                case _:
                    print('Opção não encontrada.')
                    continue

    except Exception as e:
        print('Opção inválida.')
        