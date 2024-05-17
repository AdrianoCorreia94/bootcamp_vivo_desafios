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

    def __str__(self) -> str:
        return f'Conta: {self.numero}, Agencia {self.agencia}'

    def info(self) -> str:
        return f'Ag: {self.agencia} Conta: {self.numero}'


class Cliente():
    contas = []

    def __init__(self, endereco) -> None:
        self.endereco = endereco

    # TODO: realizar transacao
    def realizar_transacao(self, transacao: object):
        self.transacao = transacao

    # TODO: adicionar conta
    def adicionar_conta(self, conta: object):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.contas = []

    def __str__(self) -> str:
        return f'Nome: {self.nome}, CPF: {self.cpf}, Nascimento: {
            datetime.date(self.data_nascimento)}, Endereco: {self.endereco}'


# ----------------------------------------------------------------------------------------------------
base_contas = {}
base_clientes = {}


def menu_opcoes():
    print('Selecione a opcao desejada\
            \n1 - Criar nova conta\
            \n2 - Ver base de dados clientes\
            \n3  Ver base de dados contas')


# testando funcionalidades
while True:
    menu_opcoes()
    op = input()
    if op == '1':
        cpf = input('Digite o CPF\n>')
        nome = input('Digite o nome do cliente\n>')
        data_nascimento = input(
            'Digite o data de nascimento do cliente (ano, mes, dia)\n>')
        endereco = input('Digite o endereco do cliente\n>')
        limite = input('Digite o limite da conta\n>')

        cliente = PessoaFisica(cpf=cpf,
                               nome=nome,
                               data_nascimento=datetime.strptime(
                                   data_nascimento, '%Y%m%d'),
                               endereco=endereco)

        conta = ContaCorrente(numero=len(base_contas)+1,
                              cliente=cliente.__str__(),
                              historico='historico',
                              limite=limite,
                              limite_saques=3)

        if cpf not in base_clientes.keys():
            base_clientes[cpf] = cliente  # adicionar a base de clientes
            base_contas[len(base_contas)+1] = conta
            cliente.adicionar_conta(conta)

        else:
            # base_contas[len(base_contas)] = conta.nova_conta()
            pass
    elif op == '2':
        for k, v in base_clientes.items():
            print(k, v)

    elif op == '3':
        for k, v in base_contas.items():
            print(k, v)

    else:
        break

for chave, valor in base_contas.items():
    print(valor.saldo, valor.limite)

# print(cliente.contas)


'''
cliente_01 = PessoaFisica(cpf='123456',
                                nome='cliente 1',
                                data_nascimento=datetime.strptime(
                                    '1994115', '%Y%m%d'),
                                endereco='Rua flores '
                                )


conta_01 = ContaCorrente(numero=1,
                         cliente=cliente_01.__str__(),
                         historico='historico',
                         limite=300,
                         limite_saques=3)

conta_02 = ContaCorrente(numero=2,
                         cliente=cliente_01.__str__(),
                         historico='historico',
                         limite=300,
                         limite_saques=3)


cliente_02 = PessoaFisica(cpf='765657',
                          nome='cliente 2',
                          data_nascimento=datetime.strptime(
                              '1904115', '%Y%m%d'),
                          endereco='Rua mar ')

conta_03 = ContaCorrente(numero=3,
                         cliente=cliente_02.__str__(),
                         historico='historico',
                         limite=300,
                         limite_saques=3)


cliente_01.adicionar_conta(conta_01.__str__())
cliente_01.adicionar_conta(conta_03.__str__())
cliente_02.adicionar_conta(conta_02.__str__())

print(cliente_01)
print(cliente_02)



clientes = []
cliente_01 = PessoaFisica(cpf='123456',
                          nome='cliente 1',
                          data_nascimento=datetime.strptime(
                              '1994115', '%Y%m%d'),
                          endereco='Rua flores ')

conta_01 = ContaCorrente(numero=1,
                         cliente=cliente_01.__str__(),
                         historico='historico',
                         limite=300,
                         limite_saques=3)

# clientes.append(cliente_01)
cpf = '123456'
base_clientes['cpf']
'''
