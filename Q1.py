from abc import ABC, abstractmethod

#criador relativo ao design pattern fábrica
class VehicleCreator(ABC):
    @abstractmethod
    def create_vehicle(self, marca, potencia):
        pass

#criador concreto de um carro com motor híbrido
class ConcreteCreatorA(VehicleCreator):
    def create_vehicle(self, marca, potencia):
        motor = MotorHibrido(potencia)
        vehicle = Automovel(motor, marca)
        return vehicle

#criador concreto de um caminhão com motor à combustão
class ConcreteCreatorB(VehicleCreator):
    def create_vehicle(self, marca, potencia):
        motor = MotorCombustao(potencia)
        vehicle = Caminhao(motor, marca)
        return vehicle

#classe que armazena tanto o tipo de automovel quanto o tipo de motor, conforme o design pattern bridge
class Veiculo:
    def __init__(self, motor, marca):
        self.motor = motor
        self.marca = marca

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

#classes contendo os subtipos possíveis de veículos
class Automovel(Veiculo):
    def __init__(self, motor, marca):
        super().__init__(motor, marca)
    def print_vehicle_type(self):
        print('Automóvel')

class Caminhao(Veiculo):
    def __init__(self, motor, marca):
        super().__init__(motor, marca)
    def print_vehicle_type(self):
        print('Caminhão')

#classes contendo os subtipos possíveis de motores empregados
class MotorEletrico(Motor):
    def __init__(self, potencia):
        super().__init__(potencia)
    def print_type(self):
        print('Motor Elétrico')

class MotorHibrido(Motor):
    def __init__(self, potencia):
        super().__init__(potencia)
    def print_type(self):
        print('Motor Híbrido')

class MotorCombustao(Motor):
    def __init__(self, potencia):
        super().__init__(potencia)
    def print_type(self):
        print('Motor à Combustão')

#exemplos de automóveis montados
automovel1 = ConcreteCreatorA().create_vehicle('Toyota', 150)
automovel1.print_vehicle_type()
automovel1.motor.print_type()

automovel2 = ConcreteCreatorB().create_vehicle('Volvo', 400)
automovel2.print_vehicle_type()
automovel2.motor.print_type()

