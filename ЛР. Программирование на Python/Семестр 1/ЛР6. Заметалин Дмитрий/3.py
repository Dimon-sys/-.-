#Вариант10
b1 = 2
b2 = 4
b = 0
n = int(input('n='))
i = 1
while i < n+1:
    if i == 1:
        b = b1
        print(b)
    elif i == 2:
        b = b2
        print(b)
    else:
        b = 6*b2 - b1
        print(b)
        b1, b2 = b2, b
    i += 1
    
