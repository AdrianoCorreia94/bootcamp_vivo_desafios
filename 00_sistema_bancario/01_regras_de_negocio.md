Segunda versao sistema bancario 
script referencia: 01_sistema_bancario.py


REGRAS DE FUNCOES JA IMPLEMENTADAS
Utilizar passagem de argumentos para as funções.
O retorno e a forma como serão chamadas fica a cargo do programador


Depositar
Apenas argumentos posicionais
Sugestão de args: saldo, valor, extrato.

Sacar
Deve receber argumentos apenas por nome (keyword only)
Sugestão de args: saldo, valor, extrato, limite, numero_saques, limite_saques

Exibir Extrato
Receber args posicionais E nomeados
Args posicionais: saldo
Args nomeados:  extrato



Novas funções:
Criar usuario (cliente)
O programa deve armazenar os usuários em uma lista de usuários.
Composta por nome, data de nascimento, cpf e endereco. 
O endereco é uma string com o formato logradouro, num - bairro - cidade/sigla estado.
Deve ser armazenado somente os números do cpf. 
Nao podem haver 2 usuários com mesmo cpf.

Criar conta corrente.
Armazenar conta em uma lista.
Conta composta por agencia, numero da conta e usuarios.
O numero da conta é sequencial iniciando em 1. 

O numero da agencia é fixo 0001.
Um usuario pode ter mais de uma conta, mas uma conta pertence somente a um usuario.

Dica
Para vincular usuario a uma conta, filtre a lista de usuarios buscando o cpf informado para cada usuario da lista.

Fique a vontade para implementar novas funções.

