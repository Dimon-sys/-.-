#Вариант10
in_ = open('1_in.txt')
out_ = open('1_out.txt', 'w')
s = 'ssssssssssssssssssssssssssssssssssss\n'

a = in_.readlines()
b = []
for i in a:
    if i == '\n':
        b.append(s)
    else:
        b.append(i)

for j in b:
    out_.write(j)

in_.close()
out_.close()
