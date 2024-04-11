# variaveis
saques_diario, extrato, saldo_atual = 0, [], 0

# criar menu de opcoes


def menu():
    print(f"\nEscolhe uma opcao")
    print(f'{" -"*9}\
          \n| 1 - Deposito\t |\
          \n| 2 - Saque\t |\
          \n| 3 - Extrato\t |\
          \n| 4 - Sair \t |\
          \n{" -"*9}')


# criar funcao de deposito
def depositar():
    # solicita o valor do deposito
    try:
        valor = float(input('Valor do deposito\n>>'))
    except:
        print('Digite um valor numerico')
    else:
        if valor < 0:  # se o valor for negativo
            print('Digite um valor inteiro positivo para deposito')  # exibir msg
        else:  # se o valor for positivo
            global saldo_atual  # usar a a variavel global que esta salvando o saldo
            # o saldo atual recebe ele mesmo + o deposito
            saldo_atual = float(saldo_atual + valor)
            extrato.append(f'Deposito R$ {valor:.2f}')  # salvar no extrato


# criar funcao de saque
def sacar():
    global saques_diario
    if saques_diario < 3:  # quantidade diaria maxima 3 saques
        try:
            valor = float(input('Valor do deposito\n>>'))
        except:
            print('Digite um valor numerico')
        else:
            if valor <= 500:  # valor maximo para saque 500
                global saldo_atual
                if saldo_atual >= valor:  # so permitir saque o valor solicitado for maior ou igual o saldo
                    # realizar o saque e subtrair o saldo
                    saldo_atual = float(saldo_atual - valor)
                    saques_diario += 1  # adicionar saque diario
                    # adicionar ao extrato
                    extrato.append(f'Saque R$ {valor:.2f}')
                else:  # se o valor do saque for menor do que o saldo, nao permitir saque
                    print("saldo indisponivel")
            else:  # se o valor solicitado para saque for maior que o limite de 500
                print('O valor máximo para saque é R$ 500,00')  # exibir msg
    else:  # se atingir o limite maximo diário
        print('Voce atingiu o limite maximo de saques por dia')


# criar funcao de extrato
def consultar_extrato():
    for op in extrato:  # para cada operacao salva no extrato
        print(op)  # exibir a operacao
    # exibir o saldo no final da lista
    print(f'Saldo Atual R${saldo_atual:.2f}')


while True:
    menu()  # funcao menu para apresentar as opcoes
    try:  # tratar erro de entrada
        op = int(input('Selecione a operacao desejada > '))  # escolha de opca
    except:  # se nao digitar numerico
        print('Digite um valor numerico')  # exibir ao usuario
        continue  # voltar ao loop
    else:  # se nao houver erro, continuar fluxo
        if op == 1:
            depositar()  # digitando 1, chamar a funcao depositar
        elif op == 2:
            sacar()  # digitando 2, chamar funcao sacar
        elif op == 3:
            consultar_extrato()  # digitando 3 chamar funcao extrato
        elif op == 4:
            print('Saindo ...')  # digitando 4 imprimir que esta saindo
            break  # sair do loop
        else:
            # qualquer outro numero, exibir mensagem da op invalida
            print('Opcao inválida, tente novamente')
            menu()  # chamar menu novamente
