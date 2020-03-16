# Generators

l1 = [num for num in range(1,11)]
l2 = (num for num in range(1,11))
print(l2)
# zip
# my_zipped_generator = zip(l1, l2)
# for item in my_zipped_generator:
#     print(item)

# print(list(my_zipped_generator))    

# map
# my_cubed_ints = map(lambda x: x ** 3, l1)
# print(list(my_cubed_ints))

my_cubed_ints = map(lambda x: x ** 3, l1)
# print(list(my_cubed_ints))
# print(next(my_cubed_ints))

def mash_map(f, some_iterable):
    for item in some_iterable:
        yield f(item)

def mash_map_2(f, some_iterable):
    return ([f(item) for item in some_iterable])


print(l1)
my_cubed_ints = mash_map(lambda x: x ** 3, l1)
print(my_cubed_ints)
# print(next(my_cubed_ints))
# print(next(my_cubed_ints))
# print(next(my_cubed_ints))
# print(list(my_cubed_ints))

