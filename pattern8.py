#diamond pattern
n=int(input("enter the number of rows: "))
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    for l in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i,n-1):
        print("*", end=" ")
    for l in range (i,n):
        print("*",end= " ")
    print()


    # to reduce one less row - from n to n-1 in outer loop of either half
    