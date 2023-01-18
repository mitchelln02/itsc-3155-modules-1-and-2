word_List = []
amount = 1
total_Word = ""
while amount != 6:  
    word = input("Enter a word: ")
    word_List.append(word)
    amount += 1
    total_Word = total_Word + " " + word
print ("Words: ",word_List)
print (f"One String:{total_Word}" ) 
