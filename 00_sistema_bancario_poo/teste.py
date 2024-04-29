# %%
class Conta():
    agencia = 1001
    _saldo = 0

    def __init__(self, conta, cliente: object) -> None:
        self.conta = conta
        self.cliente = cliente

    def criar_conta(self):
        return {'cliente': self.cliente,
                'conta': self.conta,
                'agencia': self.agencia}

    def saldo(self):
        return self._saldo


class Cliente():
    def __init__(self, nome) -> None:
        self.nome = nome

    def cadastrar_pessoa(self):
        return self.nome


# %%
clientes = {}

nome = 'Elvis'
pessoa = Cliente(nome)
clientes[1] = pessoa.cadastrar_pessoa()

conta = 1

contas = {}
conta_elvis = Conta(conta, pessoa.nome)
contas[conta] = conta_elvis.criar_conta()

# %%
print(contas)
# %%
conta_elvis.saldo()

# %%


class Transacao():
    def __init__(self, conta, valor) -> None:
        self.conta = conta
        self.valor = valor

    def depositar(self):
        return self.conta