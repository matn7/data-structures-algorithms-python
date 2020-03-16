truth_condition = True

if truth_condition:
    print("Truth")

choice = '1'
made_payment = False

if choice == '1' and made_payment:
    print("You have chosen option 1")
elif choice == '2':
    print("You have chosen option 2")    
else:
    print("You have made an invalid choice")
    
course = 'python'
a = 'enrolled in python course'
b = 'enrolled in some other course'

print(a) if course == 'python' else print(b)