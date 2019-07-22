# user expectation yields multiple related objects
# no need to know which family until runtime

# Solution:
# Abstract factory: pet factory
# Concrete factory: dog factory and cat factory
# Abstract product
# Concrete product: dog and dog food; cat and cat food

# no abstract classes or inheritance required since p3 is a dynamically typed language


class Dog:
    # One of the objects to be returned


    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    # Concrete factory

    def get_pet(self):
        # Returns a dog object
        return Dog()

    def get_food(self):
        # returns a dog food object
        return "Dog Food!"

class Cat:
    # One of the objects to be returned


    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


class CatFactory:
    # Concrete factory

    def get_pet(self):
        # Returns a cat object
        return Cat()

    def get_food(self):
        # returns a cat food object
        return "Cat Food!"


class PetStore:
    # housing the abstract factory
    # actually an instance of that

    def __init__(self, pet_factory=None):
        # pet_factory is the abstract factory as an arg
        self._pet_factory = pet_factory
        # that's all it takes to store the instance of the concrete factory

    def show_pet(self):
        # utilty to display the details of the objects returned by the DogFactory
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}.")
        print(f"Our pet says hello by this: {pet.speak()}")
        print(f"Our pet is eating {pet_food}")


# Creating / instantiating a concrete factory
factory = DogFactory()

# create a pet store housing the abstract factory with an instance of the concrete factory
shop = PetStore(factory)

# invoke
shop.show_pet()
