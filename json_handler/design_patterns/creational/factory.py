from abc import ABCMeta, abstractclassmethod

class IPet(metaclass= ABCMeta):

    @abstractclassmethod
    def pet_method():
    # inetrface method
        pass

class Dog(IPet):
    def __init__(self):
        self._name = "dog Name"
    
    def pet_method(self):
        print("Woof!")
        
class Cat(IPet):
    def __init__(self):
        self._name = "cat name"
    
    def pet_method(self):
        print("Meow!")
    
class PetFactory:
    
    # factory method
    @staticmethod
    def get_pet(Pet_type):
        if Pet_type =="Dog":
            return Dog()
        if Pet_type =="Cat":
            return Cat()
        print("Invalid Type")
        return -1

if __name__ == "__main__":
    choice = input("What type of pet do you want to create?\n")
    pet =PetFactory.get_pet(choice)
    pet.pet_method()




# Abstract base class IPet defines an interface with pet_method().
# Dog and Cat inherit and implement pet_method() with specific sounds.
# PetFactory has a static method get_pet() that creates Dog or Cat based on input.
# User chooses "Dog" or "Cat".
# get_pet() creates the object and calls its pet_method() (printing sounds).