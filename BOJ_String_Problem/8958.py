test_Case = int(input())

arr =[]
total = 0

for test in range(test_Case):
    s = input()
    for i in s:
        arr.append(i);
    jumsu =1
    total =0
    for i in arr:
        if i == 'X':
            jumsu=1
        else:
            total+=jumsu
            jumsu+=1
    arr = []
    print(total)

