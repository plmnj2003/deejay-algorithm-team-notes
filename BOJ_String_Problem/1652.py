n  = int(input())
room = [list(input()) for _ in range(n)]

row ,col =0,0
for i in range(n):
    cnt = 0
    for j in range(n):
        if room[i][j] =='.' and j < n-1:
            cnt+=1
        elif room[i][j] =='.' and j == n-1: ##벽일 경우
            cnt+=1
            if cnt>=2:
                row+=1
        elif room[i][j] =='X':
            if cnt>=2:
                row+=1
            cnt = 0

for j in range(n):
    cnt =0
    for i in range(n):
        if room[i][j] =='.' and i<n-1:
            cnt+=1
        elif room[i][j] =='.' and i==n-1:
            cnt+=1
            if cnt>=2:
                col+=1
        elif room[i][j] =='X':
            if cnt>=2:
                col+=1
            cnt =0

print(row,col)




