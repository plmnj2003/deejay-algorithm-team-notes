n = int(input())
line = list(map(int, input().split()))

######오름차순으로 정렬
line.sort()
sum_partial = 0
sum_total = 0
######
if n==1:
    print(line[0])
else:
   for i in range(n):
    for j in range(0, i + 1):
        sum_total += line[j]

print(sum_total)
#
# 1 2 3 4 5
# a[1],a[2],a[3],a[4],a[5]
#
# 1+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)