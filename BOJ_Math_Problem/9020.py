import math
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    min = 10000;
    prime_map =[False]*10000
    for i in range(2,n):
        if(isPrime(i)):
            prime_map[i] = True

    for k in range(n//2,1,-1):
        if prime_map[k] & prime_map[n-k]:
            print(k,n-k)
            break
###################################################시간초과
##에라토스테네스 채로 다시 한번 풀어보기
