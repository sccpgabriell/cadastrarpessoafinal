from datetime import date

class Endereco:
    def __init__(self, logradouro="", numero="", endereco_comercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial = endereco_comercial

class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        if endereco is None:
            endereco = Endereco()
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self):
        return self.rendimento 

class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:

            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
        super().__init__(nome, rendimento, endereco)
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def calcular_imposto(self):
        if self.rendimento <= 1500:
            return 0
        elif 1500 < self.rendimento <= 3500:
            return (self.rendimento / 100) * 2
        elif 3500 < self.rendimento <= 6000:
            return (self.rendimento / 100) * 3.5 
        else:
            return self.rendimento * 5

class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj="", nomeFantasia=""):
        if endereco is None:
            endereco = Endereco()
        super().__init__(nome, rendimento, endereco)
        self.cnpj = cnpj
        self.nomeFantasia = nomeFantasia

    def calcular_imposto(self):
        return self.rendimento * 0.10 
