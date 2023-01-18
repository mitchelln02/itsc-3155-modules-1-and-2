grade_input = int(input("What is the grade that you want to check?"))
if grade_input >= 90 and grade_input <= 100:
    print ('That grade is an A')
elif grade_input >= 80 and grade_input < 90:
        print ('That grade is an B') 
elif grade_input >= 70 and grade_input < 80:
        print ('That grade is an C')
elif grade_input >= 60 and grade_input < 70:
        print ('That grade is an D')
elif grade_input < 60 and grade_input >= 0:
        print ('That grade is an F')