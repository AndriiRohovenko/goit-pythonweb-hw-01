from abstract_factory import VihicleFactory
from vihicles import Car, Motorcycle


class USVihicleFactory(VihicleFactory):
    def __init__(self):
        self.spec = "(US Spec)"

    def create_car(self, make: str, model: str):

        return {"vihicle": Car(make=make, model=model), "spec": self.spec}

    def create_motorcycle(self, make: str, model: str):
        return {"vihicle": Motorcycle(make=make, model=model), "spec": self.spec}


class EUVihicleFactory(VihicleFactory):

    def __init__(self):
        self.spec = "(EU Spec)"

    def create_car(self, make: str, model: str):

        return {"vihicle": Car(make=make, model=model), "spec": self.spec}

    def create_motorcycle(self, make: str, model: str):

        return {"vihicle": Motorcycle(make=make, model=model), "spec": self.spec}
