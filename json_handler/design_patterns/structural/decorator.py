class Coffee:
    def __init__(self):
        self.ingredients = ["coffee beans", "hot water"]

    def brew(self):
        print("Brewing coffee with:", self.ingredients)
        return "Black coffee"

class FlavorDecorator(Coffee):
    def __init__(self, coffee, flavor):
        super().__init__()
        self.coffee = coffee
        self.flavor = flavor

    def brew(self):
        coffee = self.coffee.brew()
        print(f"Adding {self.flavor} to {coffee}")
        return f"{coffee} with {self.flavor}"

# Base coffee
base_coffee = Coffee()
print(base_coffee.brew()) 

# Coffee with caramel
caramel_coffee = FlavorDecorator(base_coffee, "caramel")
print(caramel_coffee.brew())  

# Coffee with cinnamon and milk (using multiple decorators)
cinnamon_milk_coffee = FlavorDecorator(caramel_coffee, "cinnamon")
cinnamon_milk_coffee = FlavorDecorator(cinnamon_milk_coffee, "milk")
print(cinnamon_milk_coffee.brew())  




# Decorator pattern dynamically adds new functionality to an object without modifying its original code.
# Coffee class represents the base brewing process (original function).
# FlavorDecorator inherits from Coffee and adds a flavor attribute.
# Its brew method calls the decorated coffee's brew (original function) and adds the flavor information.
# Different decorator instances are created for caramel, cinnamon, and milk, demonstrating reusability.
# By applying decorators sequentially, we create customized coffee with combined flavors (functionalities).