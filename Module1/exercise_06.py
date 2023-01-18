arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
row = int(input("enter the number for the row between 1-5 : "))
col = int(input("enter the number for the column between 1-5 : "))

arr[row-1][col-1] = 1
print (arr[0])
print (arr[1])
print (arr[2])
print (arr[3])
print (arr[4])
