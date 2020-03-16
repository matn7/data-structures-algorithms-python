my_list = [15, 7, 88, 5, 33, 14, 16, 8, 88]

my_strings_list = ["majki", "puszek", "okruszek"]
my_new_list = ["art", "econ"]

print("majki" in my_strings_list)
print(my_strings_list.index("puszek"))
print(len(my_strings_list))
print(my_strings_list[len(my_strings_list) - 1])
print(my_strings_list[- 1])
print(min(my_list))
print(dir(my_list))
print(my_list.count(15))

print("Add/remove...")
print(my_list.append(25))
my_list.insert(4, 35555)
print(my_list)

my_strings_list.extend(my_new_list)
print(my_strings_list)

my_strings_list.pop()
print(my_strings_list)

my_strings_list.remove("okruszek")
print(my_strings_list)

print(my_list[-1])
my_list[-1] = 1000
print(my_list)

print(my_list[:5])

my_list.reverse()
print(my_list)

for item in my_list:
    print(item)
    