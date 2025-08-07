sex=input()
salary=int(input())
if(sex=="m" and salary<10000):
    salary=salary*0.7
    print(salary)
elif(sex=="f" and salary<10000):
    salary=salary*.12
    print(salary)
elif(sex=="m"):
    salary=salary*.5
    print(salary)
else:
    salary=salary*.10
    print(salary)
