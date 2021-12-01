import sys
n,k  = map(int,sys.stdin.readline().split())
thermal =list(map(int,sys.stdin.readline().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = thermal[i-1]+dp[i-1]

answer = -9999999
for i in range(n):
    start = i
    end = i+k
    if end < n+1:
        answer = max(dp[end]-dp[i],answer)

print(answer)

