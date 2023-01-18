even_list = []
all_list = []
x = 1
w = 0
while x != quit:
    x = input("enter a number or QUIT to quit : ")
    if str(x) == 'quit':
        break
    w = int(x)
    all_list.append(x)
    if(w % 2 == 0):
        even_list.append(w)

print ('The even list is: ', even_list)
print ('The all list is: ', all_list)

