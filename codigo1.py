class Estudante:
    def _init__(self, nome, email):
        self.nome = nome
        self.email = email

lista = []

def adicionar_lista(Estudante):
    lista.append(Estudante)
    print("Estudante cadastrado com sucesso!")


