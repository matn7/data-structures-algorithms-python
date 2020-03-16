node_1 = "custom object"

# Lists
my_data_type = [1, 2, False, None, "majka", 5.0, node_1]
print(my_data_type)
print(type(my_data_type))
print(my_data_type[4])

# Dictionaries
my_dictionary = {1: "hello", 2: "majka"}
print(my_dictionary)
print(my_dictionary[1])
print(type(my_dictionary))

# Sets
my_sets = {1, 2, False, None, "majka", 5.0, node_1, "majka"}
print(my_sets)
print(type(my_sets))

# Tuples - Immutable
my_tuple = (1, 2, False, None, "majka", 5.0, node_1)
print(my_tuple)
print(my_tuple[5])
# my_tuple[5] = "python"
print(type(my_tuple))