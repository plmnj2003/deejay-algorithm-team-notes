n, k = map(int, input().split())
thing = [[0,0]]

d = [[0]*(k+1) for _ in range(n+1)]
for i in range(n):
    thing.append(list(map(int, input().split())))

print(thing)