from abstract_factory import Vihicle


class Car(Vihicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")


class Motorcycle(Vihicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")
