#动态规划

def dp(n):
    if n==0 or n==1:
        return 0
    else:
        result=0
        for i in range(1,n+1):
            for j in range(1,i):
                result=max(result,j*(i-j),j*dp(i-j))
        return result

n=int(input())
print(dp(n))

