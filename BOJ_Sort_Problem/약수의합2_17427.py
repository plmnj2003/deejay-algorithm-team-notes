#
# def sum_divisor(a):
#     sum = 0
#     for i in range(1,a+1):
#         if a%i ==0:
#             sum+=(a//i)
#         else:
#             continue
#     return sum
#
#
# A = int(input())
# total =0
# for i in range(1,A+1):
#     total += sum_divisor(i)
#
# print(total)

n = int(input())

sum = 0

for i in range(1, n+1) :
  sum += (n//i)*i
print(sum)

