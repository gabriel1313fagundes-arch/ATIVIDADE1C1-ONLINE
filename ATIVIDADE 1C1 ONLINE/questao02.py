# Cria a classe Animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade  # Idade privada

    # Consulta a idade
    def get_idade(self):
        return self.__idade

    # Modifica a idade
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
            print("Idade alterada com sucesso!")
        else:
            print("A idade não pode ser negativa!")

    # Exibe os dados
    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.__idade)

    # Som do gato
    def emitir_som(self):
        print("Miau!")


# Cria o gato
gato = Animal("Mimi", 2)

# Mostra os dados iniciais
gato.exibir_dados()

# Permite digitar uma nova idade
nova_idade = int(input("Digite a nova idade do gato: "))

# Altera a idade
gato.set_idade(nova_idade)

# Mostra a idade atualizada
print("Idade atual:", gato.get_idade())

# Emite o som
gato.emitir_som()