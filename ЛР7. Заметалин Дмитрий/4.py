#Вариант10
s = input('строка с пробелами: ').lower()
s = s.replace(' ', '')
if s == s[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
