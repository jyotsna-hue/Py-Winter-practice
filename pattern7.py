n=int(input("enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i,n-1):
        print("*", end=" ")
    for l in range(i,n):
        print("*", end=" ")
    print()

# one less column - from n to n-1 in any one decreasing star 
#one less column - from i+1 to i in any one increasing star