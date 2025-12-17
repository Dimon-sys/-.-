n = int(input())
potomok_predok = dict()
for i in range(n-1):
    l = input()
    potomok = l.split(' ')[0]
    predok = l.split(' ')[1]
    potomok_predok[potomok] = predok

while True:
    po_1, po_2 = input().split(' ')[0], input().split(' ')[0]
    