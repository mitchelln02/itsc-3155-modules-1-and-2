string1 = input("Enter a string:" )
letter_List = list(string1)
big_List = []

for x in range(0,len(letter_List),3):
    little_List = []

    for i in range(0,3):
        if (x+i)<len(letter_List):
            little_List.append(letter_List[x+i])
    big_List.append(little_List)
print(big_List)        
