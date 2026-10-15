# Classe principal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    # Consulta a idade
    def get_idade(self):
        return self.__idade

    # Exibe os dados
    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.get_idade())


# Classes que herdam de Animal
class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

class Passaro(Animal):
    pass


# Cria os animais
cachorro = Cachorro("Rex", 4)
gato = Gato("Mimi", 2)
passaro = Passaro("Piu", 1)


# Mostra os dados de cada animal
print("Cachorro:")
cachorro.exibir_dados()

print("\nGato:")
gato.exibir_dados()

print("\nPássaro:")
passaro.exibir_dados()