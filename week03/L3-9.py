n=int(input()) #输入一个整数n

list_a=list() #创建空列表

for num in range(0,n):
    y=int(input()) #输入数组a
    list_a.append(y) #在列表末尾加入新元素

#print(list_a)

list_b=list()
list_b.append(list_a[0])

for num in range(1,n):
    x=1
    for i in range(0,num):
        x=x*list_a[i]
    for j in range(num+1,n):
        x=x*list_a[j]
    list_b.append(x)

print(list_b)