# Cria a classe Animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Exibe os dados do animal
    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)

    # Emite o som do gato
    def emitir_som(self):
        print("Miau!")


# Cria um objeto da classe Animal
gato = Animal("Mimi", 2)

# Exibe os dados do gato
gato.exibir_dados()

# Exibe o som do gato
gato.emitir_som()