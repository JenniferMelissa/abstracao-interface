from modulo import * 

if __name__ == '__main__':
    cc = ContaCorrente('','','1001-1','10010-1',0)

    #entrada de dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o CPF do titular: ')

    #saida de dados
    print(f' Nome: {cc.nome}.')
    print(f' CPF: {cc.cpf}.')
    print(f' Agência: {cc.agencia}.')
    print(f' Conta: {cc.conta}.')
    print(f' Saldo: {cc.saldo}.')

    print('\n')

    try:
        while True:
            print('SAQUE E DEPOSITO')
            print('1 - Saque.')
            print('2 - Deposito.')
            print('3 - Sair do programa.')

            opcao = int(input('Informe a opção desejada: '))

            match opcao:
                case 1:
                    valor_saque = float(input('Informe valor a ser sacado: '))
                    saque = cc.fazer_saque(valor_saque)
                    if saque is not None:
                        print(f'Valor sacado: {saque}.')
                        continue
                    else:
                        print('Não é possível fazer o saque. Escolha outra opção')
                        continue
                        

                case 2: 
                    valor = float(input('Informe valor a ser depositado: '))
                    deposito = cc.fazer_deposito(valor)
                    print(f'Novo Saldo: {deposito}.')
                    continue
                
                case 3:
                    print('Programa encerro.')
                    break
                case _:
                    print('Opção não encontrada.')
                    continue

    except Exception as e:
        print('Opção inválida.')
        