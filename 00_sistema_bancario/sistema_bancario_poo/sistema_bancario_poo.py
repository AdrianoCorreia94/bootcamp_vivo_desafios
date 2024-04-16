# %%


# ---------------------- CLASSES ----------------------


class Cliente():
    def __init__(self, endereco, contas: list):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: object, transacao: object):
        pass

    def adiconar_conta(conta: object):
        pass


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas: list, nome: str, data_nascimento, cpf: str):
        super().__init__(endereco, contas)
        self.nome = nome
        self.data_nascimento = None
        self.cpf = cpf
        self.contas = None

    def __str__(self) -> str:
        return f'Nome: {self.nome} \nNascimento: {self.data_nascimento} \nCPF: {self.cpf}'

    def cadastrar_pessoa_fisica(self):
        cadastro = {'nome': self.nome,
                    'nascimento': self.data_nascimento,
                    'cpf': self.cpf,
                    'endereco': self.endereco}
        base_clientes[self.cpf] = cadastro

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# ------------------ FUNCOES ------------------

# %%
def cadastrar_cliente():  # funcao para criar um novo cliente
    global cadastros
    # entrada de cpf, excluindo-se espacos vazios e pontos
    cpf = str(input('digite o cpf do cliente\n> ').strip().replace('.', ''))

    if not consultar_cpf(cpf):  # se o CPF nao está cadastrado, prosseguir com cadastro
        nome = str(input('Digite o nome do cliente\n> '))  # nome do cliente

        endereco = cadastrar_endereco()

        cliente = PessoaFisica(
            contas= [],
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


# %%
cadastrar_cliente()
# %%
print(base_clientes)
