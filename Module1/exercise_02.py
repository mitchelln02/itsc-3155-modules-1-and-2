String1 = input('Enter first word to check')
String2 = input('Enter second word to check')
if String1.endswith(String2) or String2.endswith(String1):
    my_bool = True
    print(my_bool)
else: 
    my_bool = False
    print(my_bool)

