#计算区间[2 3]上的定积分：∫(x^2+4*x*sin(x))dx

import random
import math

def f(x):
    return x*x+4*x*math.sin(x)

def monte_carlo_integration(func,a,b,n): #func传递函数参数
    total=0
    for i in range(n):
        x=random.uniform(a,b)
        sum=func(x)
        total+=sum
    average=total/n
    integral=(b-a)*average
    return integral

result=monte_carlo_integration(f,a=2,b=3,n=1000000)

print(result)

