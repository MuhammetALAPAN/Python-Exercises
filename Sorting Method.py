

def insertion_sort(my_list, length):
    """
        Sorting Method
    """
    for i in range(1, length):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key


# test case
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
numbers = [12, 11, 13, 5, 6]

insertion_sort(cars, len(cars))
insertion_sort(numbers, len(numbers))

print(", ".join(cars))
print(numbers)
