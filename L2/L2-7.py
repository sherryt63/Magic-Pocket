#牛顿迭代法公式：Xn+1=Xn-f(Xn)/f'(Xn)

c=int(input()) #求c的三次方根
x=2

while(abs(x**3-10)>0.000001):
    x=2*x/3+c/(3*x*x)

print(x)
