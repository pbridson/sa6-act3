from functools import reduce

number = 195437
number_string = str(number)
number_list = map(lambda x: int(x), number_string)

sum = reduce(lambda x, y: x + y, number_list)

print (f"The sum of the digits in {number} is {sum}.")

