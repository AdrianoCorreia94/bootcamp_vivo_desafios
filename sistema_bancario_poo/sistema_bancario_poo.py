# %%


# ---------------------- CLASSES ----------------------


class Cliente():
    def __init__(self, endereco, contas: list):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: object, transacao: object):
        transacao.registrar(conta)

    def adiconar_conta(self, conta: object):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas: list, nome: str, data_nascimento, cpf: str):
        super().__init__(endereco, contas)
        self.nome = nome
        self.data_nascimento = None
        self.cpf = cpf
        self.contas = None

    def __str__(self) -> str:
        return f'Nome: {self.nome} \nNascimento: {self.data_nascimento} \nCPF: {self.cpf}'


class Conta():
    def __init__(self, numero: int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self) -> float:
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente: object, numero: int):
        return cls(cliente, numero)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor: float):
        valor_saque = valor
        self._saldo -= valor_saque


class ContaCorrente(Conta):
    pass

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# ------------------ FUNCOES ------------------
# %%
def menu():

    print(f"\nEscolhe uma opcao")

    print(f'{" -"*9}\
          \n| 1 - Deposito\t |\
          \n| 2 - Saque\t |\
          \n| 3 - Extrato\t |\
          \n| 4 - Sair \t |\
          \n{" -"*9}')


# %%
def cadastrar_cliente():  # funcao para criar um novo cliente
    global cadastros
    # entrada de cpf, excluindo-se espacos vazios e pontos
    cpf = str(input('digite o cpf do cliente\n> ').strip().replace('.', ''))

    if not consultar_cpf(cpf):  # se o CPF nao está cadastrado, prosseguir com cadastro
        nome = str(input('Digite o nome do cliente\n> '))  # nome do cliente

        endereco = cadastrar_endereco()

        cliente = PessoaFisica(
            contas=[],
            data_nascimento='',
            nome=nome,
            cpf=cpf,
            endereco=endereco
        )
        cliente.cadastrar_pessoa_fisica()
        cadastros += 1

    else:  # se CPF ja estiver cadastrado
        print('CPF já cadastrado')  # exibir mensagem


def cadastrar_endereco():  # funcao cadastrar endereco do cliente
    logradouro = str(input('Insira o logradouro do cliente\n> '))
    num = str(input('Insira o numero do cliente\n>  '))
    bairro = str(input('Insira o bairro do cliente\n>  '))
    cidade = str(input('Insira a cidade do cliente\n>  '))
    estado = str(input('Insira sigal do estado do cliente\n> '))
    endereco = (f'{logradouro},{num}- {bairro}- {cidade}/{estado}')
    # retornar endereco como string com logradour numero, bairro - cidade/siglaEstado
    return endereco


def consultar_cpf(cpf: str):  # funcao para consultar se o CPF já esta cadastrado
    cpf = cpf
    return cpf in base_clientes.keys()  # retornar F or T para CPF encontrado

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# %%
# ------------------ OBJETOS ------------------
base_clientes = {}  # salvar base de dados de clientes
cadastros = 1   # contador automa
contagem_contas = 1  # contagem de clientes cadastrados
contas_cadastradas = {}  # base de dados contas
saldo_atual = float(0)  # saldo atual da conta
extrato = []  # extrato
saques_diario = 0  # contagem de saque diario


# --------- PROGRAMA PRINCIPAL ---------
# %%
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
