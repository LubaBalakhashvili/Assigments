from datetime import datetime

class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1

    def car_info(self):
        print("Car Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def age_of_car(self):
        current_year = datetime.now().year
        age = current_year - self.year
        return age

    @classmethod
    def total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"The battery life of this machine is {self.battery_life} hours")


car1 = Car("Toyota", "Camry", 2020)
Car.total_cars()
car1.car_info()
print(car1.age_of_car())

electric_car = ElectricCar("Tesla", "Model S", 2022, 500)
Car.total_cars()
electric_car.car_info()
print(electric_car.age_of_car())
