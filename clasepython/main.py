from clasepython.model.car import Car

def main():

    carro: Car = Car("Nissan",2020,4)

    carro.move(4)
    carro.speed(True)

    print(carro.distance_traveled)
    print(carro.__velocidad)


if __name__ == "__main__":
    main()


