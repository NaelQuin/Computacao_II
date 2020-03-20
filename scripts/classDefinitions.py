"""
Classes e objetos
"""

class Conta():
    """Classe destinada para criar a categoria Conta

       Conta(nome=str, cpf=str, saldo=float) -> object
    """

    def __init__(self, nome, cpf, senha='1234', saldo=0.0):
        "Metodo construtor"

        # Abrindo arquivo com id das contas
        arquivoContas = open('contas.txt','r+')

        # Lendo numero de contas
        numerosContas = arquivoContas.readlines()

        # Gerando numero desta conta
        self.numeroConta = int(numerosContas[-1][:-1]) + 1        

        # Adicionando novo numero de conta no arquivo
        arquivoContas.write("%d\n"%self.numeroConta)

        # Fechando arquivo (Evitar corrupção dos dados)
        arquivoContas.close()

        # Definindo o atributo 'nome'
        self.nome = nome

        # Definindo o atributo 'cpf'
        self.cpf = cpf

        # Definindo o atributo 'saldo'
        self.saldo = saldo

        # Definindo o atributo 'senha'
        self.senha = senha

        return None

    def __str__(self):
        "Método Mágico: chamado pela função 'print'"

        # Delimitador para exibição
        delimitador = 80*'-'

        # Pergunte se deseja exibir o saldo
        if (input("\n*Digite a senha para exibir os dados: ") != self.senha):
            # Montando mensagem de exibição
            apresentação = delimitador+'\n'\
                           +"Dados não autorizados\n"\
                           +delimitador+'\n'

        # Senha correta
        else:             
            # Montando mensagem de exibição
            apresentação = \
'''
%s
Conta: %d

Nome : %s

Cpf  : %s

Saldo: %s
%s
'''%(delimitador,
     self.numeroConta,
     self.nome.capitalize(),
     self.cpf,
     self.saldo,
     delimitador)

        return apresentação

    def obtem_saldo(self):
        return self.saldo

#minha_conta = Conta('Natanael Quintino', '12260613705')
