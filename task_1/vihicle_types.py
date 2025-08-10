from abstract_factory import VihicleFactory
from vihicles import Car, Motorcycle


class USVihicleFactory(VihicleFactory):
    def __init__(self):
        self.make = "(US Spec)"

    def create_car(self, model: str):
        return Car(model + " " + self.make)

    def create_motorcycle(self, model: str):
        return Motorcycle(model + " " + self.make)


class EUVihicleFactory(VihicleFactory):

    def __init__(self):
        self.make = "(EU Spec)"

    def create_car(self, model: str):
        return Car(model + " " + self.make)

    def create_motorcycle(self, model: str):
        return Motorcycle(model + " " + self.make)
