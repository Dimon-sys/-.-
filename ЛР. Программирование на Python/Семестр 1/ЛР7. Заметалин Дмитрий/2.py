#Вариант10
s = input().lower().replace(' ','').replace(',','').replace(':','').replace('-','').replace(';','')
c = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
print(c)
        
