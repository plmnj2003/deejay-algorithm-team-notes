n,k = map(int,input().split())
g =[0]*(n+1)
map = [[0]*(k+1)]*(n+1)
for i in range(1,n+1):
    g[i] = int(input())

for i in range(1,n+1):
    if i%2==0:
        for j in range(g[i]):
            map[j][i-1] = 1
    else:
        for j in range(g[i]):
            print(n-i+1,i+1)


print(map)
