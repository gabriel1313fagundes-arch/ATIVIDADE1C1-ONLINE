# Classe principal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    # Consulta a idade
    def get_idade(self):
        return self.__idade

    # Modifica a idade
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("A idade não pode ser negativa!")

    # Exibe os dados
    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.get_idade())

    # Som padrão
    def emitir_som(self):
        print("O animal está emitindo um som")


# Classe Cachorro
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")


# Classe Gato
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")


# Classe Louro (pássaro)
class Louro(Animal):
    def emitir_som(self):
        print("Louro está cantando: Piu piu!")


# Cria os objetos
cachorro = Cachorro("Rex", 4)
gato = Gato("Mimi", 2)
louro = Louro("Louro", 1)


# Exibe os dados e os sons
print("Cachorro:")
cachorro.exibir_dados()
cachorro.emitir_som()

print("\nGato:")
gato.exibir_dados()
gato.emitir_som()

print("\nLouro:")
louro.exibir_dados()
louro.emitir_som()