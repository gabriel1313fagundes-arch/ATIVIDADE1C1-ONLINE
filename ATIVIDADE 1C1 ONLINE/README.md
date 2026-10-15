# Atividade de Programação

## Identificação do estudante

- Nome: Gabriel oliveira f santos
- Curso: programador de sistemas
- Disciplina: Programação
- Professor: Murilo
- Data: 15/10/2026

## Respostas das questões teóricas
## 7. Respostas das questões teóricas

### a) Qual é a função da classe Animal no sistema? Como ela representa a abstração?

A classe Animal serve como modelo para criar diferentes tipos de animais, contendo características e métodos comuns, como nome, idade e emitir som. Ela representa a abstração porque reúne as características essenciais dos animais, sem precisar detalhar tudo sobre cada espécie.

### b) Por que utilizamos __idade em vez de deixar o atributo totalmente acessível?

Utilizamos __idade para proteger o atributo, dificultando o acesso direto a ele fora da classe. Isso permite controlar como a idade é consultada ou alterada, ajudando a evitar valores inválidos, como uma idade negativa.

### c) Qual é a vantagem de utilizar herança nas classes Cachorro, Gato e Passaro?

A herança permite que as classes Cachorro, Gato e Passaro aproveitem os atributos e métodos da classe Animal. Isso evita a repetição de código, facilita a manutenção e permite que cada classe tenha suas próprias características.

### d) Por que o método emitir_som() apresenta resultados diferentes para cada animal?

Isso acontece por causa do polimorfismo. Cada classe pode implementar o método emitir_som() de maneira diferente, fazendo com que o cachorro lata, o gato mie e o pássaro cante.

### e) O que aconteceria se tentássemos cadastrar um animal com idade negativa? Como o programa poderia impedir isso também no momento da criação do objeto?

Se o programa não tiver uma validação, poderá aceitar uma idade negativa, o que não faz sentido nesse contexto. Para impedir isso durante a criação do objeto, podemos validar a idade no método __init__ e lançar um erro com raise ValueError caso ela seja negativa.

###Exemplo de código para a letra E

# Esta classe representa um animal
class Animal:

    # Essas variveis inicializa o animal com nome e idade
    def __init__(self, nome, idade):

        # Verifica se a idade é maior ou igual a zero
        if idade >= 0:

            # Armazena o nome do animal
            self.nome = nome

            # Armazena a idade 
            self.__idade = idade

        else:
            # Exibe uma mensagem caso a idade seja negativa
            print("A idade não pode ser negativa!")