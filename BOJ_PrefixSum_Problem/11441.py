import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
k = int(input())
dp =[0]*(n+1)
for i in range(1,n+1):
    dp[i] = dp[i-1]+arr[i-1]
for _ in range(k):
     i,j = map(int,sys.stdin.readline().split())
     answer = dp[j]-dp[i-1]
     print(answer)
