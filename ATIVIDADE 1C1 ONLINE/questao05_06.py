# Classe principal
class Animal:
    # Inicializa o nome e a idade do animal
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    # Consulta a idade do animal
    def get_idade(self):
        return self.__idade

    # Modifica a idade do animal
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("A idade não pode ser negativa!")

    # Exibe o nome e a idade do animal
    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.get_idade())

    # Define o som padrão do animal
    def emitir_som(self):
        print("O animal está emitindo um som")


# Classe Cachorro herda da classe Animal
class Cachorro(Animal):
    # Sobrescreve o som do cachorro
    def emitir_som(self):
        print("Au au!")


# Classe Gato herda da classe Animal
class Gato(Animal):
    # Sobrescreve o som do gato
    def emitir_som(self):
        print("Miau!")


# Classe Louro herda da classe Animal
class Louro(Animal):
    # Sobrescreve o som do louro
    def emitir_som(self):
        print("Louro está cantando: Piu piu!")


# Questão 5

# Cria o objeto cachorro
cachorro = Cachorro("Rex", 4)

# Cria o objeto gato
gato = Gato("Mimi", 2)

# Cria o objeto louro
louro = Louro("Louro", 1)


# Questão 6

# Cria uma lista contendo os três objetos
animais = [cachorro, gato, louro]

# Mostra a lista inteira com os nomes dos animais
print("LISTA COMPLETA DE ANIMAIS:")

print([animal.nome for animal in animais])

print("----------------")

# Percorre todos os objetos da lista
for animal in animais:

    # Exibe o nome e a idade do animal
    animal.exibir_dados()

    # Exibe o som específico de cada animal
    animal.emitir_som()

    # Separa os animais
    print("----------------")