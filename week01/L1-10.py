import sys

S=input()
len_s=len(S)-1

i=0

while(i<len_s):
    if(S[i]==S[i+1]):
        print("TRUE")
        sys.exit(0)  #类似于return 0直接跳出程序
    else:
        i+=1

print("FALSE")