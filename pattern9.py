#butterfly 
n=int(input("Enter the number of rows: "))
for  i in range(n-1):
    for j in range(i+1):
        print("*", end=" ")
    for k in range (i,n):
        print(" ", end=" ")
    for l in range(i,n):
        print(" ",end=" ")
    for m in range(i+1):
        print("*", end=" ") 
    print()
for o in range(n):
    for p in range(o,n):
        print("*", end=" ")
    for q in range(o+1):
        print(" ", end=" ")
    for r in range(o+1):
        print(" ",end= " ")
    for s in range(o,n):
        print("*",end=" ")
    print()
