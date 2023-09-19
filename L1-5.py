x=input()
y=input()
z=input()
#输入上述三个数字时候要换行

temp_1=0
temp_2=0
temp_3=0

if(x>y):
    temp_1=x
    x=y
    y=temp_1

if(x>z):
    temp_2=x
    x=z
    z=temp_2

if(y>z):
    temp_3=y
    y=z
    z=temp_3

print(x,y,z)

