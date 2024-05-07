# Abstract Factory interface
class FurnitureFactory:
    def create_chair(self):
        raise NotImplementedError

    def create_table(self):
        raise NotImplementedError

# Concrete Factories - Modern and Classic styles
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_table(self):
        return ClassicTable()

# Abstract Products - Base chair and table
class Chair:
    def sit(self):
        raise NotImplementedError

class Table:
    def put_things(self):
        raise NotImplementedError

# Concrete Products - Modern and Classic chairs and tables
class ModernChair(Chair):
    def sit(self):
        print("Sitting on a sleek modern chair")

class ModernTable(Table):
    def put_things(self):
        print("Putting things on a modern glass table")

class ClassicChair(Chair):
    def sit(self):
        print("Sitting on a comfortable classic chair")

class ClassicTable(Table):
    def put_things(self):
        print("Putting things on a sturdy classic wood table")


# Client code uses the factory to create furniture
factory = ModernFurnitureFactory()
chair = factory.create_chair()
table = factory.create_table()

chair.sit()  # Output: Sitting on a sleek modern chair
table.put_things()  # Output: Putting things on a modern glass table

# Switch to classic style easily
factory = ClassicFurnitureFactory()
chair = factory.create_chair()
table = factory.create_table()

chair.sit()  # Output: Sitting on a comfortable classic chair
table.put_things()  # Output: Putting things on a sturdy classic wood table

