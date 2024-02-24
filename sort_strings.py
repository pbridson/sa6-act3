input_list = ["function","set", "list", "array", "string", "number", "data"]

# length_list = list(map(lambda x: len(x), input_list))

# tuple_list = list(map(lambda x, y: (x,y), length_list, input_list))

# alpha_sort = sorted(input_list)

# output = sorted(alpha_sort, key=lambda x: len(x))

input_list.sort(key=lambda x: (len(x),x))

print(input_list)
      

