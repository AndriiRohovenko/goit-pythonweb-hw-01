from vihicle_types import USVihicleFactory, EUVihicleFactory
from logger import logging_info


if __name__ == "__main__":
    us_factory = USVihicleFactory()
    eu_factory = EUVihicleFactory()

    mustang = us_factory.create_car("Ford Mustang")
    harley = us_factory.create_motorcycle("Harley-Davidson")

    bmw = eu_factory.create_car("BMW M3")
    ducati = eu_factory.create_motorcycle("Ducati")

    logging_info(mustang.model)
    logging_info(harley.model)
    logging_info(bmw.model)
    logging_info(ducati.model)
