# clones objects according to prototypical instance
# used when many identical objects individually are to be created (otherwise expensive)

# Scenario: mass production for cars
# Solution: create prototypical instance and clone when necessary

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self,name,obj):
        # register the object that should be cloned
        # take the name arg as key and the object instance as value
        self._objects[name] = obj

    def unregister_object(self,name):
        # delete the object stored in the dict
        del self._objects[name]

    def clone(self,name,**attr):
        # pull the object from the dict, clone the object and update its attr

        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


# the prototypical object slated for replication
class Car:
    def __init__(self):
        self.name = "Toyota"
        self.color = "White"
        self.options = "TB"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.options}"


# instantiate
c = Car()
# create prototype object out of the prototype class
prototype = Prototype()
# register the c var
prototype.register_object('Toyota', c)

c1 = prototype.clone('Toyota')

print(c1)
