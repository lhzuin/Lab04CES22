
# classe que armazena o objeto final construído (um pedaço de pizza)
class PizzaComponent:
    def getDescription(self): # retorna itens presentes na pizza
        return self.__class__.__name__

    def getTotalCost(self): # retorna o preço total do produto
        return self.__class__.cost

# classe que apresenta uma definição recursiva para a pizza, retornando o valor e descrição após a adição de cada um dos ingredientes
class Decorador(PizzaComponent):
    def __init__(self, pizza_component):
        self.component = pizza_component
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ', ' + PizzaComponent.getDescription(self)

# lista de ingredientes
# cada classe contém um valor, e pode receber uma instância de PizzaComponent, de forma que o Decorador adiciona o ingrediente atual a pizza montada somente depois que o ingrediente interno é adicionado
class Prato(PizzaComponent):
    cost = 0.00

class MassaFina(Decorador):
    cost = 2.0
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class MassaGrossa(Decorador):
    cost = 4.0
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class Mussarela(Decorador):
    cost = 1.50
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class Frango(Decorador):
    cost = 3.00
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class Catupiry(Decorador):
    cost = 2.00
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class Calabresa(Decorador):
    cost = 2.50
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class MolhoDeTomate(Decorador):
    cost = 2.00
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

class Tomate(Decorador):
    cost = 1.25
    def __init__(self, pizza_component):
        Decorador.__init__(self, pizza_component)

#Exemplos de possíveis pizzas montadas
pizza_frango_catupiry = Frango(Catupiry(Mussarela(MolhoDeTomate(MassaGrossa(Prato())))))
print(pizza_frango_catupiry.getDescription()+ ": R$" + str(pizza_frango_catupiry.getTotalCost()))

pizza_calabresa = Calabresa(MolhoDeTomate(MassaFina(Prato())))
print(pizza_calabresa.getDescription()+ ": R$" + str(pizza_calabresa.getTotalCost()))