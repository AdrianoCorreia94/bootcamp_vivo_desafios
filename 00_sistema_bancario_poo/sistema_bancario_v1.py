from abc import ABC, abstractmethod
from datetime import date, datetime


class Conta():
    agencia = '0001'
    _saldo = 0

    def __init__(self, numero, cliente, historico):
        self.numero = numero
        self.cliente = cliente
        self.historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo

    def nova_conta(self):
        return {'Agencia: ': self.agencia, 'Conta:': self.numero, 'cliente': self.cliente}

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self) -> str:
        return f'Agencia: {self.agencia}\nNumero{self.numero}'


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, historico, limite, limite_saques):
        super().__init__(numero, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques


class Cliente():
    contas = []

    def __init__(self, endereco) -> None:
        self.endereco = endereco

    # TODO: realizar transacao
    def realizar_transacao(self, transacao: object):
        self.transacao = transacao

    # TODO: adicionar conta
    def adicionar_conta(self, conta: object):
        self.conta = conta


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def cadastrar_cliente(self):
        return {'nome': self.nome,
                'cpf': self.cpf,
                'data_nascimento': f'{datetime.date(self.data_nascimento)}',
                'endereco': self.endereco,
                'contas': self.contas}

    def __str__(self) -> str:
        return f'Nome: {self.nome}, CPF: {self.cpf}, Nascimento: {
            datetime.date(self.data_nascimento)}, Endereco: {self.endereco}'


# ----------------------------------------------------------------------------------------------------

base_contas = {}
base_clientes = {}


def menu_opcoes():
    print('Selecione a opcao desejada\
            1 - Cadastrar Cliente\
            2 - Criar nova conta\
            3 - Ver base de dados clientes\
            4 - Ver base de dados contas')


def criando_conta():
    cpf = input('Digite o CPF\n>')
    nome = input('Digite o nome do cliente\n>')
    data_nascimento = input(
        'Digite o data de nascimento do cliente (ano, mes, dia)\n>')
    endereco = input('Digite o endereco do cliente\n>')
    limite = input('Digite o limite da conta\n>')

    # TODO: instanciar pessoa para passar como parametro para criar conta
    cliente = PessoaFisica(cpf=cpf,
                           nome=nome,
                           data_nascimento=datetime.strptime(
                               data_nascimento, '%Y%m%d'),
                           endereco=endereco)

    base_clientes[cliente.cpf] = cliente.cadastrar_cliente()

    conta = ContaCorrente(numero=1,
                          cliente=cliente.__str__(),
                          historico='historico',
                          limite=limite,
                          limite_saques=3)

    base_contas[len(base_contas)] = conta.nova_conta()


# testando funcionalidades
while True:
    menu_opcoes()
    op = input()
    if op == '1':
        cpf = input('Digite o CPF\n>')
        if cpf not in base_clientes.keys():
            nome = input('Digite o nome do cliente\n>')
            data_nascimento = input(
                'Digite o data de nascimento do cliente (ano, mes, dia)\n>')
            endereco = input('Digite o endereco do cliente\n>')

            cliente = PessoaFisica(cpf=cpf,
                                   nome=nome,
                                   data_nascimento=datetime.strptime(
                                       data_nascimento, '%Y%m%d'),
                                   endereco=endereco)

            atualizar = cliente.cadastrar_cliente()
            base_clientes[cliente.cpf] = atualizar

        else:
            print('cliente já cadastrado no sistema')
            break
    elif op == '2':
        criando_conta()

    elif op == '3':
        for k, v in base_clientes.items():
            print(k, v)

    elif op == '4':
        for k, v in base_contas.items():
            print(k, v)

    else:
        break
