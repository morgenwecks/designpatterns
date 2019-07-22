class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


# Passed args will be stored as dict object
# Default value here is Sell


def get_pet(pet="Dog"):

    # The factory method

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())