c=int(input())

g=c/2 #寻找c的平方根g

i=0 #循环次数i

while(abs(g**2-c)>0.0000000001):
    g=(g+c/g)/2
    i=i+1
    print("%d:%.13f"%(i,g))

