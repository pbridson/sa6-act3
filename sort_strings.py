input_list = ["function","set", "list", "array", "string", "number", "data"]

# Method 1: presort alphabetically
# alpha_sort = sorted(input_list)
# output_list = sorted(alpha_sort, key=lambda x: len(x))

# Method 2: convert list to tuples
# length_list = list(map(lambda x: len(x), input_list))
# tuple_list = list(map(lambda x, y: (x,y), input_list, length_list))
# alpha_sort = sorted(tuple_list, key=lambda alpha: alpha[0])
# length_sort = sorted(alpha_sort, key=lambda length: length[1])
# output_list = list(map(lambda x: x[0], length_sort))

# Method 3: sort keys in tuple
output_list = sorted(input_list, key=lambda x: (len(x), x))

print(f"Input:  {input_list}")
print(f"Output: {output_list}")
      

