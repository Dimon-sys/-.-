#Вариант10
n = int(input())
k = 0
while 3**(k+1) < n:
    k += 1
print(k)
