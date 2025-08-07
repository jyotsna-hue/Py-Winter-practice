x=int(input())
if(x%4==0 and x%100!=0):
    print("is a leap year")
elif(x%4==0 and x%400):
    print("is a leap year")
else:
    print("is not a leap year")
