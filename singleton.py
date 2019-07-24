# Problem: allow only one object to be instantiated
# Creating global variable in an oop way

# Scenario: Need to keep cache of information to be shared by multiple objects
# Solution: Module
# The Borg design pattern


class Borg:
    # Borg class making class attributes global
    # attribute dictionary

    _shared_state = {}

    def __init__(self):
        # Initialize the instance, but take attributes from the state:
        # Turn the shared state into an updated attribute dictionary of the class for all future instances
        self.__dict__ = self._shared_state


class Singleton(Borg): # inherits from the Borg class
    # This class now shares all its attributes among its various instances
    # Essentially makes the singleton objects an object-oriented variable

    def __init__(self, **kwargs):
        # Call the init method, inheriting the existing shared state
        Borg.__init__(self)
        # Update the attribute dict by inserting a new kv-pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # returns the attribute dict for printing
        return str(self._shared_state)


# create a singleton object and add the first acronym
x = Singleton(HTTP="Hypertext Transfer Protocol")


# print it
print(x)

# create another singleton object, if it refers to the same attribute dict by adding another acronym

y = Singleton(SNMP="Simple Network Management Protocol")

# print the object
print(y)