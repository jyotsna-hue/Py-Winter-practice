#right sided triangle 
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i,n):
        print(" " , end = " ")
    for k in range(i+1):
        print("*", end =" ")
    print()