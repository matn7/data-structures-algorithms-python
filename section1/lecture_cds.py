my_dictionary = {'name': 'mashrur', 'course': 'python', 'fav_food': 'ice cream'}
phone_dict = {'mashrur': '555-55-5555',
              'zoolander': '999-99-9999',
              'jon_snow': 'fail-o-so-bad'}
word_dict = {'a':
                {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor'
                },
             'b':
                {
                 'bad': 'of poor quaity or low standard',
                 'business': 'season 8 of GOT'
                }
            }

print(word_dict)
print(word_dict['b'])
print(word_dict['b']['business'], word_dict['b']['bad'])
print(my_dictionary.get('name'))
my_dictionary['job'] = 'python programmer'
print(my_dictionary.get('job'))
my_dictionary['course'] = 'java'
print(my_dictionary.get('course'))

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

for k, v in my_dictionary.items():
    print(k, v)

# Tuples - Immutable
my_random_tuple = ('first',1,7,6,4,5,8,'hi there',2,3,1,5,2,1,9,10)
my_tuple = ('first_value','second_value','third_value')

print(my_random_tuple[-1])
print(my_random_tuple[::-1])

print(dir(my_random_tuple))
print(len(my_random_tuple))
print(my_random_tuple.count(5))
print(my_random_tuple.index('hi there'))

first_var, second_var, third_var = my_tuple
print(third_var)

print('first' in my_random_tuple)

for item in my_random_tuple:
    print(item)

# Sets - unordered, duplicates, finding info, math operations
my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python'}
print(my_set)
my_list = [1,6,2,'java','ruby',8,9,10,21,1000,6,'python','java']
print(my_list)
my_set = set(my_list)
print(my_set)
print('java' in my_set)
programming_set = {'java','ruby','javascript','python','c'}
print(my_set.intersection(programming_set))
print(my_set.union(programming_set))
print(my_set.difference(programming_set))
print(programming_set.difference(my_set))

for item in my_set:
    print(item)
