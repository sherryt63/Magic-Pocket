#第一种：调用math库
import math

pi = math.pi
print(pi)


#第二种：蒙特卡洛法
import random

n=1000000
count=0
for i in range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)

    if(x*x+y*y<=1):
        count+=1

pi=4*count/n
print(pi)


#第三种：莱布尼茨级数（Π/4=1-1/3+1/5-1/7+...）
n=1000000
sum=0
count=0

for i in range(1,n,2):
    sum+=1/i*((-1)**count)
    count+=1

pi=sum*4
print(pi)
    
