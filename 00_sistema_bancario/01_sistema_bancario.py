#%%

clientes = {}   # base de clientes
cadastros = 1   # contador automa
contagem_contas = 1  # contagem de clientes cadastrados
contas_cadastradas = {}  #  base de dados contas 
saldo_atual = float(0)  # saldo atual da conta
extrato = []  # extrato
saques_diario = 0  # contagem de saque diario


def menu():  # funcao para apresentar menu, sem funcionalidades
    print(f"\nEscolhe uma opcao")

    print(f'{" -"*9}\
          \n| 1 - Deposito\t |\
          \n| 2 - Saque\t |\
          \n| 3 - Extrato\t |\
          \n| 4 - Sair \t |\
          \n{" -"*9}')


def cadastrar_cliente():  # funcao para criar um novo cliente
    global cadastros
    cpf = str(input('digite o cpf do cliente\n> ').strip().replace('.', ''))  # entrada de cpf, excluindo-se espacos vazios e pontos
    if not consultar_cpf(cpf):  # se o CPF nao está cadastrado, prosseguir com cadastro
        nome = str(input('Digite o nome do cliente\n> '))  # nome do cliente
        data_nascimento = str(
            input('Digite a data de nascimento do cliente \n> '))  # data nascimento
        endereco = cadastrar_endereco()
        cadastro = {'nome': nome,
                    'nascimento': data_nascimento,
                    'cpf': cpf,
                    'endereco': endereco}  #dicionario local com o cadastro
        clientes[cpf] = cadastro  # inserir o dicionario local na base global de clientes, usando como chave o CPF
        cadastros += 1
    else:  # se CPF ja estiver cadastrado
        print('CPF já cadastrado')  # exibir mensagem


def cadastrar_endereco(): # funcao cadastrar endereco do cliente
    logradouro = str(input('Insira o logradouro do cliente\n> ')) 
    num = str(input('Insira o numero do cliente\n>  '))
    bairro = str(input('Insira o bairro do cliente\n>  '))
    cidade = str(input('Insira a cidade do cliente\n>  '))
    estado = str(input('Insira sigal do estado do cliente\n> '))
    endereco = (f'{logradouro},{num}- {bairro}- {cidade}/{estado}')
    return endereco # retornar endereco como string com logradour numero, bairro - cidade/siglaEstado


def consultar_cpf(cpf: str):  # funcao para consultar se o CPF já esta cadastrado
    cpf = cpf
    return cpf in clientes.keys() # retornar F or T para CPF encontrado


def criar_conta():  # funcao para criar uma nova conta
    global contagem_contas  # contagem de contas, para num. automatico da conta
    agencia = '0001'  # numero da agencia pre definida
    cliente = str(input('CPF do cliente ')) # CPF do cliente dono da conta
    contas_cadastradas[contagem_contas] = {
                                            'numero_conta': contagem_contas, 
                                            'agencia': agencia, 
                                            'cliente': cliente
                                            }   # adicionar a conta no dict de contas com chave automatica
    contagem_contas += 1 # incrementar no numero automatico de conta


def depositar(valor: float, saldo: float, extrato: list):  # funcao realizar deposito
    novo_saldo = saldo + valor  # novo saldo recebe saldo atual + valor do deposito
    extrato.append(f'Deposito R$ {valor:.2f}') # extrato adiciona a operacao à list de extrato
    return novo_saldo  # retornar o novo saldo apos operacao
    

def sacar(*, valor: float, saldo: float, extrato: list):  # funcao sacar
    global saques_diario   # contagem de saques diarios realizados
    if valor > 500:  # valor maior que o maximo permitido
        print('Valor maximo do permitido para saque')
    elif valor < 0: # valor negativo, nao permitido
        print('Valor invalido')
    else: # valores positivos abaixo do limite maximo
        novo_saldo = saldo - valor  # novo saldo recebe saldo atual - valor do saque 
        extrato.append(f'Saque R$ {valor}')  # adicionar a operacao ao extraro
        saques_diario += 1  # saques diarios incremente 1 
        return novo_saldo  # retornar o novo saldo apos a operacao


# criar funcao de extrato
def consultar_extrato():
    for op in extrato:  # para cada operacao salva no extrato
        print(op)  # exibir a operacao
    print(f'Saldo Atual R${saldo_atual:.2f}')  # exibir o saldo no final da lista


while True:
    menu()  # funcao menu para apresentar as opcoes
    
    try:  # tratar erro de entrada
        op = int(input('Selecione a operacao desejada > '))  # escolha de opca
    
    except:  # se nao digitar numerico
        print('Digite um valor numerico')  # exibir ao usuario
        continue  # voltar ao loop
    
    else:  # se nao houver erro, continuar fluxo
        
        if op == 1:
            try:  # tratamento para garantir que seja digitado um inteiro
                valor_deposito = float(input('Valor do deposito\n>>'))  # solicitar valor para deposito
            
            except:  # se o ususario nao digitar um valor numerico
                print('\n\tdigite um valor inteiro positivo') # exibir mensagem de falha 
                pass

            else:  # se nao houver erro
        
                if valor_deposito <= 0:  # se o valor do deposito for negativo ou zero, nao sera aceito
                    print('\n\tvalor invalido para deposito')
                
                else:  # se estiver dentro do permitido
                    saldo_atual = depositar(valor_deposito, saldo_atual, extrato)  # chamar a funcao depositar

        elif op == 2:  # opcao 2, realizar saque
 
            if saques_diario >= 3:  # se o cliente atingiu a quantidade maxima diaria de saques
                print('\n\tLimite de saques diarios atingidos')  # exibir mensagem 
 
            else:  # se nao atingiu a quantidade maxima diaria

                try:  # forcar entrada numerica para valor do saque
                    valor_saque = float(input('\n\tValor para saque\n>>'))

                except:  # se o usuario digitar um valor nao numerico
                    print('\n\tdigite um valor inteiro positivo') # exibir mensagem de falha

                else:  # se o usuario digitar numeros inteiros
                    
                    if valor_saque <= 0:  # forcar um valor positivo diferente de zero
                        print('\n\tDigite valor positivo')
                    
                    elif valor_saque > saldo_atual:  # se o valor pra saque for maior que saldo
                        print('\n\tSaldo insuficiente') # impedir operacao exibindo mensagem

                    else:   # estando tudo dentro das normas
                        saldo_atual = sacar(valor=valor_saque, saldo=saldo_atual, extrato=extrato)  # chamar funcao sacar
               
        elif op == 3:  # opcao 3 consultar o extrato
            consultar_extrato()  # chamar funcao extrato
        
        elif op == 4:  # opcao encerrar
            print('Saindo ...')  # imprimir que esta saindo
            break  # sair do loop
        
        else:
            # qualquer outro numero, exibir mensagem da op invalida
            print('\n\tOpcao inválida, tente novamente')
            menu()  # chamar menu novamente
