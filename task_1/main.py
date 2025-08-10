from vihicle_types import USVihicleFactory, EUVihicleFactory

if __name__ == "__main__":
    us_factory = USVihicleFactory()
    eu_factory = EUVihicleFactory()

    mustang = us_factory.create_car("Ford Mustang")
    harley = us_factory.create_motorcycle("Harley-Davidson")

    bmw = eu_factory.create_car("BMW M3")
    ducati = eu_factory.create_motorcycle("Ducati")

    print(mustang.model)
    print(harley.model)
    print(bmw.model)
    print(ducati.model)
