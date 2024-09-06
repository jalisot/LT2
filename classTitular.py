class Titular():
    def __init__ (self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome 
    
    def get_sobrenome(self):
        return self.sobrenome
    
    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome 

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"




class Conta(object):
    def __init__(self, numero, o_titular, saldo, limite=1000.0):
        self.numero = numero
        self.o_titular = o_titular
        self.saldo = saldo
        self.limite = limite


    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero

    def get_o_titular(self):
        return self.o_titular
    
    def set_o_titular(self, o_titular):
        self.o_titular

    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self, saldo):
        self.saldo

    def get_limite(self):
        return self.limite
    
    def set_limite(self, limite):
        self.limite

    def get_nomeTitular(self):
        return self.o_titular.get_nome()
    
    def get_nomeTitular(self):
        return self.o_titular.get_sobrenome()
    
    def get_nomeTitular(self):
        return self.o_titular.get_cpf()
    

    











