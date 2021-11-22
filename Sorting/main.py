n = int(input())
numbers = []
for _ in range(n):
  numbers.append(int(input()))

##Bubble Sort
for i in range(len(numbers)):
  for j in range(len(numbers)):
    if numbers[i]<numbers[j]:
      numbers[i],numbers[j] = numbers[j],numbers[i]

for i in range(len(numbers)):
  print(numbers[i])


##버블 정렬
