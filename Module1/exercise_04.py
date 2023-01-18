amountInList = int(input('Enter the amount of numbers you want to enter: '))
my_list = []
total = 0
x = 1
while x < amountInList+1: 
    user_Input = float(input(f'Enter Number {x} : ' ))
    my_list.append(user_Input)
    x += 1
    total = total + user_Input
print (my_list)
print (total/amountInList)