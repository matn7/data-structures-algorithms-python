# def my_math_func(x, f):
#     return f(x)

# def x_cube(x):
#     return x ** 3

# my_lambda = lambda x: x ** 3
# print(my_math_func(5, lambda x: x ** 3))
# print(my_lambda(5))

# my_letters = ['a', 'b', 'c', 'd', 'e']

# print(list(map(str.capitalize, my_letters)))

# print(list(map(lambda x:x+x.capitalize(), my_letters)))

from random import randint

my_ints = [randint(1, 1000) for num in range(100)]

print(list(map(lambda x:x ** 3, my_ints)))
