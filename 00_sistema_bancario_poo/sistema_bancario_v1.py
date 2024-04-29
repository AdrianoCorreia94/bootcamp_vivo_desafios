# %%
from datetime import date, datetime
from abc import ABC, abstractmethod


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


class Transacao(ABC):
    @abstractmethod
    def registrar(self):
        pass


class Deposito(Transacao):
    def __init__(self, deposito) -> None:
        super().__init__()
        self.deposito = deposito

    def registrar(self):
        pass


class Saque(Transacao):
    def __init__(self, deposito) -> None:
        super().__init__()
        self.deposito = deposito

    def registrar(self):
        pass

# ---------------------------------------------------------------


def menu_opcoes():
    print('Selecione a opcao desejada\
            1 - Cadastrar Cliente\
            2 - Criar nova conta\
            3 - Ver base de dados clientes\
            4 - Ver base de dados contas')


# ---------------------------------------------------------------
# MAIN ---

base_clientes = {}


# ----------
while True:
    menu_opcoes()
    op = input()
    if op == '1':
        cpf = input('Digite o CPF\n>')
        if cpf not in base_clientes.keys():
            nome = input('Digite o nome do cliente\n>')
            data_nascimento = input('Digite o data de nascimento do cliente (ano, mes, dia)\n>')
            endereco = input('Digite o endereco do cliente\n>')

            cliente = PessoaFisica(cpf=cpf,
                                   nome=nome,
                                   data_nascimento=datetime.strptime(data_nascimento, '%Y%m%d'),
                                   endereco=endereco)

            atualizar = cliente.cadastrar_cliente()
            base_clientes[cliente.cpf] = atualizar

        else:
            print('cliente já cadastrado no sistema')
            break

    elif op == '3':
        print(base_clientes)

    else:
        break
