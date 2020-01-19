class Car:
    """
    Класс машины Car, у которого есть поля: марка и модель автомобиля.
    Поля задаются через конструктор
    """
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def __str__(self):
        return f"Машина: {self.mark} - {self.model}"

class Garage:
    """
    Класс гаража Garage, у которого есть поле списка машин.
    Поле задается через конструктор.
    По аналогии с классом Company из лекции реализован интерфейс итерируемого.
    Реализованы методы add и delete(удалять по индексу) машин из гаража
    """
    def __init__(self, cars):
        if list != type(cars):
            raise ValueError("Конструктор принимает список!")
        self.cars = cars

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        if len(self.cars) > index:
            del self.cars[index]

    def __str__(self):
        return f"Гараж: {self.cars}"


if __name__ == '__main__':
    car = Car("Hyundai", "Elantra")
    assert car.mark == "Hyundai" and car.model == "Elantra"

    garage = Garage([car])
    assert len(garage) == 1 and car in garage

    car2 = Car("BMW", "X5")
    garage.add(car2)
    assert len(garage) == 2 and car2 in garage

    garage.delete(1)
    assert len(garage) == 1 and car in garage and car2 not in garage
