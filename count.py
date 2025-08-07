
sump=sumn=summ=0
count=0
while(1):
    n=int(input())
    if(n==-1):
        break
    elif(n<0):
        sumn=sumn+n
        print(sumn)
    elif(n>0):
        sump=sump+n
        print(sump)
    elif(n==0):
        #summ=summ+n(0+0=0)
        count=count+1
        print(count)
