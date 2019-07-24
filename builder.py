
# Is a solution to the telescoping constructor Anti Pattern
# Problem: too many constructors
# Scenario: car building requires too many parts to be constructed and then assembled
# Solution: 4 different roles, director, abstract builder(interfaces), concrete builder (impletents the interfaces)
# Product: object being built
# Complexity reduction by device and conquer, not by inheritance.


class Director():
    # Director
    def __init__(self,builder):
        # the instance of the particular type of builder class is passed as a argument to the class
        # and initiated as an internal object
        self._builder = builder

    def construct_car(self):

        # invoking now the internal instance of the particular builder that had been passed

        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    # Abstract builder
    def __init__(self):

        # start empty

        self.car = None

    def create_new_car(self):

        # after instantiated and class method is invoked, create an instance of car

        self.car = Car()


class SkyLarkBuilder(Builder):
    # concrete builder - provides parts and tools to work on the parts

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car():
    # product
    # after invoked, create empty slate attributes that are then combined by the abstract builder
    # as it has information about the make
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f"{self.model} | {self.tires} | {self.engine}"


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
