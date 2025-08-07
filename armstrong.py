x=int(input())
ones=x%10
twos=(x//10)%10
threes=x//100
if(ones**3+twos**3+threes**3==x):
    print("yes")
else:
    print("no")