from abstract_factory import Vihicle
from logger import logging_info


class Car(Vihicle):
    def start_engine(self):
        logging_info("Car engine started")

    def stop_engine(self):
        logging_info("Car engine stopped")


class Motorcycle(Vihicle):
    def start_engine(self):
        logging_info("Motorcycle engine started")

    def stop_engine(self):
        logging_info("Motorcycle engine stopped")
