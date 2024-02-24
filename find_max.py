from functools import reduce

numbers = [12, 6, 9, 15, 1, 3, 1, 13]

max_number = reduce(lambda x, y: x if x > y else y, numbers)

print(f"The maximum number in the list is: {max_number}.")