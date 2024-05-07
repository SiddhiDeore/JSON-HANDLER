class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

class InsertionSort:
    def sort(self, data):
        # Implement insertion sort algorithm
        sorted_data = []
        for element in data:
            index = 0
            while index < len(sorted_data) and element > sorted_data[index]:
                index += 1
            sorted_data.insert(index, element)
        return sorted_data

class BubbleSort:
    def sort(self, data):
        # Implement bubble sort algorithm
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(data) - 1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
        return data

# Usage example
unsorted_data = [5, 2, 8, 1, 3]

insertion_sorter = Sorter(InsertionSort())
sorted_data = insertion_sorter.sort(unsorted_data.copy())
print("Insertion Sort:", sorted_data)

bubble_sorter = Sorter(BubbleSort())
sorted_data = bubble_sorter.sort(unsorted_data.copy())
print("Bubble Sort:", sorted_data)


# The Strategy pattern allows you to dynamically switch algorithms at runtime by encapsulating them in separate objects.
# Sorter class represents the main sorting application, holding a concrete sorting strategy object.
# InsertionSort and BubbleSort provide different sorting algorithms by implementing the sort method.
# The sort method in Sorter delegates the actual sorting to the encapsulated strategy's sort method.
# This allows swapping between different sorting strategies (InsertionSort, BubbleSort) without modifying the Sorter class.