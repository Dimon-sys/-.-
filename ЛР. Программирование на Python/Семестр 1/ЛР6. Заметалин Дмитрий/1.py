#Вариант10
x = int(input())
for i in range(2, x+1):
    s = 0
    for g in range(1, i+1):
        if i % g == 0:
            s += g
    if s == i:
        print(i)
