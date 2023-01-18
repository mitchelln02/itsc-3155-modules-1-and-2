String = input("Enter a string: ")
Uppercase = ""
Lowercase = ""

for x in String:
    if x.isupper():
        Uppercase += x
    elif x.islower():
        Lowercase += x

End = Lowercase + Uppercase
print (End)