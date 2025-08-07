countn=countu=countl=0
while(1):
    x=input()
    if(x=="*"):
        break
    elif x.isupper():
        countu=countu+1
        print(countu)
    elif x.islower():
        countl=countl+1
        print(countl)
    elif x.isnumeric():
        countn=countn+1
        print(countn)
    else:
        print("enter valid ")

    
