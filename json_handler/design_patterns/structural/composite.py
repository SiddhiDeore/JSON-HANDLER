class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def list(self, level=0):
        print(f"  " * level + self.name + f" ({self.size} bytes)")

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def list(self, level=0):
        print(f"{self.name}/")
        for child in self.children:
            child.list(level + 1)

# Create file system hierarchy
root = Directory("root")
home = Directory("home")
user = Directory("user")
documents = Directory("documents")
file1 = File("file1.txt", 100)
file2 = File("file2.pdf", 500)

user.add_child(documents)
documents.add_child(file1)
documents.add_child(file2)
home.add_child(user)
root.add_child(home)

# List the entire file system
root.list()


# Composite pattern allows you to treat groups of objects as single objects, creating tree-like structures.
# File represents individual files with a name and size.
# Directory represents folders with a name and a list of children (files or other directories).
# Both File and Directory inherit a list method for displaying their information.
# Directory's list method iterates through its children, calling their list method recursively, creating a tree-like traversal.
# Building the hierarchy demonstrates how groups are treated as single units.