from abc import ABC, abstractmethod


class Vehicle(ABC):
    brand = ""

    def __init__(self, brand) -> None:
        self.brand = brand

    @abstractmethod
    def print_info(self):
        pass


class Car(Vehicle):
    engine = 2.8

    def __init__(self, brand, engine) -> None:
        super().__init__(brand)
        self.engine = engine

    def print_info(self):
        print("Car is", car.brand, ', engine capacity is', car.engine)


class Bus(Vehicle):

    def __init__(self, brand, number_of_sitting_places=32) -> None:
        super().__init__(brand)
        self.number_of_sitting_places = number_of_sitting_places

    def print_info(self):
        print("Bus is", bus.brand, ', number of sitting place is', bus.number_of_sitting_places)


class Flight(Vehicle):

    def __init__(self, brand, max_speed=856) -> None:
        super().__init__(brand)
        self.max_speed = max_speed

    def print_info(self):
        print("Flight is", flight.brand, ', max speed is', flight.max_speed)


class Trolleybus(Vehicle):

    def __init__(self, brand, number_of_staff=2) -> None:
        super().__init__(brand)
        self.number_of_staff = number_of_staff

    def print_info(self):
        print("Trolleybus is", trolleybus.brand, ', number of staff is', trolleybus.number_of_staff)


class Tram(Vehicle):

    def __init__(self, brand, based_capacity=48) -> None:
        super().__init__(brand)
        self.based_capacity = based_capacity

    def print_info(self):
        print("Tram is", tram.brand, ", based capacity is", tram.based_capacity)


car = Car('BMW', 3.2)
bus = Bus('Bogdan', 32)
flight = Flight('MAY', 856)
trolleybus = Trolleybus('Etalon', 2)
tram = Tram('Electron', 48)

car.print_info()
bus.print_info()
flight.print_info()
trolleybus.print_info()
tram.print_info()
