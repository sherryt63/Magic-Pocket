#g改为c

c=int(input())

g=c #寻找c的平方根g

i=0 #循环次数i

while(abs(g**2-c)>0.0000000001):
    g=(g+c/g)/2
    i=i+1
    print("%d:%.13f"%(i,g))
#运行结果同g=c/2时一样，故无影响


#g改为c/4
c=int(input())

g=c/4 #寻找c的平方根g

i=0 #循环次数i

while(abs(g**2-c)>0.0000000001):
    g=(g+c/g)/2
    i=i+1
    print("%d:%.13f"%(i,g))
#运行结果同g=c/2时一样，故无影响