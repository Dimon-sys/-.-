#Вариант10
in_ = open('2_in.txt', encoding='utf-8')
out_ = open('2_out.txt', 'w', encoding='utf-8')

a = in_.readlines()
l = []
b = [s.split(' ') for s in a]
for j in b:
    for i in j:
        l.append(i.replace(',', '').replace('.', '').replace(':', '').replace(';', '').replace('(', '').replace(')', '').replace('-', '').replace('!', '').replace('?', '').replace('"', '').replace('\n', ''))

print(l)
for k in l:
    if k.upper()[0] == 'С':
        out_.write(k+'\n')

in_.close()
out_.close()
