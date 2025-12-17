#Вариант10
t = input('текст: ')
t = t.split(' ')
digits = []
for i in t:
    if i.isdigit():
        digits.append(int(i))
print(max(digits))
