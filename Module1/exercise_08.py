x = 1
list = []
single_List = []
while x != 11:
    value = int(input(f'Enter number {x}: '))
    list.append(value)
    x += 1
for x in list:
    if list.count(x) == 1:
        single_List.append(x)
print (list)
print(single_List)