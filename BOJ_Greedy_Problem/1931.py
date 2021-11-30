n = int(input())
data = []
meeting_count =0
last_time =0

for _ in range(n):
    start, end = map(int,input().split())
    data.append([start,end])

data = sorted(data,key = lambda a:a[0])
data = sorted(data,key = lambda a:a[1])

for i,j in data:
    if i>=last_time:
        meeting_count+=1
        last_time = j
print(meeting_count)