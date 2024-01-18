#输出固定位数的二进制数

x=int(input())
result=bin(x)[2:] #bin函数将数字转化为二进制
                  #[2:]意味着对字符串进行【切片】，把开头的0b删除
length=len(result)

digit=int(input()) #希望输出的位数
if(digit>=length):
    zeros='0'*(digit-length)
    print(zeros+result)
else:
    print(result)