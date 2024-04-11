#%%

clientes = {}
cadastros = 1
contagem_contas = 1
contas_cadastradas = {}
saldo_atual = float(0)
extrato = []
saques_diario = 0

def menu():
    print(f"\nEscolhe uma opcao")

    print(f'{" -"*9}\
          \n| 1 - Deposito\t |\
          \n| 2 - Saque\t |\
          \n| 3 - Extrato\t |\
          \n| 4 - Sair \t |\
          \n{" -"*9}')


def criar_usuario():
    global cadastros
    cpf = str(input('digite o cpf do cliente\n> ').strip())
    if not consultar_cpf(cpf):
        nome = str(input('Digite o nome do cliente\n> '))
        data_nascimento = str(
            input('Digite a data de nascimento do cliente \n> '))
        endereco = cadastrar_endereco()
        cadastro = {'nome': nome,
                    'nascimento': data_nascimento,
                    'cpf': cpf,
                    'endereco': endereco}
        clientes[cpf] = cadastro
        cadastros += 1
    else:
        print('CPF já cadastrado')


def cadastrar_endereco():
    logradouro = str(input('Insira o logradouro do cliente\n> '))
    num = str(input('Insira o numero do cliente\n>  '))
    bairro = str(input('Insira o bairro do cliente\n>  '))
    cidade = str(input('Insira a cidade do cliente\n>  '))
    estado = str(input('Insira sigal do estado do cliente\n> '))
    endereco = (f'{logradouro},{num}- {bairro}- {cidade}/{estado}')
    return endereco


def consultar_cpf(cpf: str):
    cpf = cpf
    return cpf in clientes.keys()


def criar_conta():
    global contagem_contas
    agencia = '0001'
    cliente = str(input('CPF do cliente '))
    contas_cadastradas[contagem_contas] = {
        'numero_conta': contagem_contas, 'agencia': agencia, 'cliente': cliente}
    contagem_contas += 1


def depositar(valor: float, saldo: float, extrato: list):
    novo_saldo = saldo + valor
    extrato.append(f'Deposito R$ {valor:.2f}')
    return novo_saldo
    

def sacar(*, valor: float, saldo: float, extrato: list):
    global saques_diario   
    if valor > 500:
        print('Valor maximo do permitido para saque')
    elif valor < 0:
        print('Valor invalido')
    else:
        novo_saldo = saldo - valor
        extrato.append(f'Saque R$ {valor}')
        saques_diario += 1
        return novo_saldo


# criar funcao de extrato
def consultar_extrato():
    for op in extrato:  # para cada operacao salva no extrato
        print(op)  # exibir a operacao
    print(f'Saldo Atual R${saldo_atual:.2f}')  # exibir o saldo no final da lista


#%%
while True:
    menu()  # funcao menu para apresentar as opcoes
    
    try:  # tratar erro de entrada
        op = int(input('Selecione a operacao desejada > '))  # escolha de opca
    
    except:  # se nao digitar numerico
        print('Digite um valor numerico')  # exibir ao usuario
        continue  # voltar ao loop
    
    else:  # se nao houver erro, continuar fluxo
        
        if op == 1:
            try:
                valor_deposito = float(input('Valor do deposito\n>>'))        
            except:
                print('\n\tdigite um valor inteiro positivo')
                pass
            else:
                if valor_deposito < 0:
                    print('\n\tvalor invalido para deposito')
                else:
                    saldo_atual = depositar(valor_deposito, saldo_atual, extrato)  # digitando 1, chamar a funcao depositar

        elif op == 2:
            if saques_diario >= 3:
                print('\n\tLimite de saques diarios atingidos')
            else:
                try:
                    valor_saque = float(input('\n\tValor para saque\n>>'))
                except:
                    print('\n\tdigite um valor inteiro positivo')
                else:
                    if valor_saque <= 0:
                        print('\n\tDigite valor positivo')
                    elif valor_saque > saldo_atual:
                        print('\n\tSaldo insuficiente')
                    else:
                        saldo_atual = sacar(valor=valor_saque, saldo=saldo_atual, extrato=extrato)  # digitando 2, chamar funcao sacar
               
        elif op == 3:
            consultar_extrato()  # digitando 3 chamar funcao extrato
        
        elif op == 4:
            print('Saindo ...')  # digitando 4 imprimir que esta saindo
            break  # sair do loop
        
        else:
            # qualquer outro numero, exibir mensagem da op invalida
            print('\n\tOpcao inválida, tente novamente')
            menu()  # chamar menu novamente
