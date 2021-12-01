import sys
n,m = map(int,sys.stdin.readline().split())
a =list(map(int,sys.stdin.readline().split()))
dp =[0]*100001
for i in range(1,n+1):
    dp[i] = dp[i-1]+a[i-1]

for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    if s ==1:
        answer = dp[e]
    else:
        answer = dp[e]-dp[s-1]
    print(answer)