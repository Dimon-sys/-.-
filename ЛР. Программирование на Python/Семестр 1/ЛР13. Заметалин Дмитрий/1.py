f = open('1_in.txt', 'r')
g = open('1_out.txt', 'w')
matrix = f.readlines()
m = ''

for i in matrix:
    m += i
m = m.split('\n')
m = [[int(j) for j in i.split(' ')] for i in m]
a = [max(i) for i in m]

for i in a:
    g.write(str(i) + ' ')
print(m)
print(a)

f.close()
g.close()