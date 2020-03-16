from random import randint, choice
from string import ascii_lowercase

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}

sum = 0;
for num in l:
    sum = sum + num

print(sum)
print(f"Sum using list: {sum}")

sum = 0
for num in range(len(l)):
    sum += l[num]

print(f"Sum using range generator: {sum}")

# run_times = int(input("How many times do you want the program to run? "))

# for num in range(run_times):
#     print(f"Run: {num+1}")

for key, value in my_dict.items():
    print(f"key is {key}, value is {value}") 

l1 = [randint(1, 100) for num in range(100)]

print(l1)

l1 = [choice(ascii_lowercase) for num in range(100)]

print(l1)

# while loops
truth_condition = True

i = 0
num_to_search = 25
l1 = [randint(1,100) for num in range(1000)]

while i < len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i += 1

for index, num in enumerate(l1):
    if num == num_to_search:
        print(f"{num_to_search} found at index {index}")
        break

# while True:
#     print("Please choose an option from the list below:")
#     print("Press 1 for selection 1")
#     print("Press 2 for selection 2")
#     print("Press 3 to quit")
#     selection = input("Enter your choice-> ")
#     if int(selection) == 3:
#         break

l1 = ['.py','.js','.rb','.java','.c']
l2 = ['python','javascript','ruby','java','c']

tupled_list = list(zip(l2, l1))
print(tupled_list)
