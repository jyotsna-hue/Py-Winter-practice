#increasing triangle
n=int(input("Enter the number of rows: "))
for i in range(n):
    for i in range(i+1):
        print("*", end=" ")
    print()
