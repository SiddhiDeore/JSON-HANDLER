from abc import ABCMeta,abstractclassmethod

class IPet(metaclass =ABCMeta):

    @abstractclassmethod
    def print_data():
        pass

class PetSingolton(IPet):
    __instance = None

    @staticmethod
    def get_instance():
        if PetSingolton.__instance == None:
            PetSingolton("Default Name",0)
        return PetSingolton.__instance
    
    def __init__(self,name) -> None:
        if PetSingolton.__instance != None:
            raise Exception("Singolton can't be instantiatiated more then one")
        else:
            self.name = name
            PetSingolton.__instance = self

    @staticmethod
    def print_data():
        print(f'name:{PetSingolton.__instance.name}')
    
p = PetSingolton("hope")
print(p)
p.print_data()

p2 = PetSingolton.get_instance()
print(p2)
p2.print_data



# Only one instance of a class can exist (centralized access point).
# Abstract base class defines interface with print_data().
# PetSingolton inherits and uses a static variable (__instance) to hold the single instance.
# get_instance() method returns the existing instance or creates a new one if needed.
# Constructor is private to prevent direct object creation.
# Call get_instance() to access the single instance.
# Methods like print_data() can access and manage data related to the "pet".