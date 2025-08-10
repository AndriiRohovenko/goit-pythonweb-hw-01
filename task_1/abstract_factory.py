from abc import ABC, abstractmethod


class Vihicle(ABC):
    def __init__(self, model: str):
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class VihicleFactory(ABC):
    @abstractmethod
    def create_car(self, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, model: str):
        pass
