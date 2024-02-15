class Car:
    def __new__(cls, *args, **kwargs):
        instance = super(Car, cls).__new__(cls)
        print("Creating a new Car instance.")
        return instance

    def __init__(self, brand=None, model=None, year=None):
        print("Initializing Car instance.")
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def set_brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("Invalid input for brand. Please provide a string.")

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        if isinstance(model, str):
            self._model = model
        else:
            print("Invalid input for model. Please provide a string.")

    def get_model(self):
        return self._model

    def set_year(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            print("Invalid input for year. Please provide an integer.")

    def get_year(self):
        return self._year


# Example usage:
car_instance = Car()
car_instance.set_brand("Toyota")
car_instance.set_model("Camry")
car_instance.set_year(2022)

print(f"Brand: {car_instance.get_brand()}, Model: {car_instance.get_model()}, Year: {car_instance.get_year()}")