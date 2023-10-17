m=int(input())
n=int(input())

x=min(m,n) #找二者的最小值

for num in range(1,x+1):
    if(m%num==0 and n%num==0):
        y=num

print(y)