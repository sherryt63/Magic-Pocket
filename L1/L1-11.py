S=input()
len_s=len(S)-1 #先计算字符串长度
S=list(S) #将字符串转为列表，因为字符串在py里不能重新赋值

i=0

while(i<len_s):
    while(S[i]==' '): #直到把所有空格去掉
        j=i
        while(j<len_s):
            S[j]=S[j+1]
            j+=1
        S[len_s]='\0'
    i+=1

S=''.join(S) #再将列表转为字符串，为了输出
print(S)