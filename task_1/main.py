from vihicle_types import USVihicleFactory, EUVihicleFactory
from logger import logging_info


if __name__ == "__main__":
    us_factory = USVihicleFactory()
    eu_factory = EUVihicleFactory()

    mustang = us_factory.create_car("Ford", "Mustang")
    harley = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    bmw = eu_factory.create_car("BMW", "X5")
    ducati = eu_factory.create_motorcycle("Ducati", "Panigale")

    logging_info(
        mustang["vihicle"].make + " " + mustang["vihicle"].model + " " + mustang["spec"]
    )
    logging_info(
        harley["vihicle"].make + " " + harley["vihicle"].model + " " + harley["spec"]
    )
    logging_info(bmw["vihicle"].make + " " + bmw["vihicle"].model + " " + bmw["spec"])
    logging_info(
        ducati["vihicle"].make + " " + ducati["vihicle"].model + " " + ducati["spec"]
    )
