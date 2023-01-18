amountInList = int(input('Enter the amount of numbers you want in list 1: '))
my_list1 = []
x = 1
while x < amountInList+1: 
    user_Input = input(f'Enter Number {x} : ' )
    my_list1.append(user_Input)
    x += 1
amountInList = int(input('Enter the amount of numbers you want in list 2: '))
my_list2 = []
x = 1
while x < amountInList+1: 
    user_Input = input(f'Enter Number {x} : ' )
    my_list2.append(user_Input)
    x += 1
my_list3 = []
my_list1_set = set(my_list1)
my_list2_set = set(my_list2)
 
if (my_list1_set & my_list2_set):
        my_list3.append(my_list1_set & my_list2_set)

print (my_list1)
print (my_list2)
print (my_list3)
