from abc import ABC, abstractmethod


class Vihicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class VihicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass
