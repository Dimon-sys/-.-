n = int(input())
potomok_predok = dict()
potomok_his_ancestors = dict()
family = []
for i in range(n-1):
    l = input()
    potomok = l.split(' ')[0]
    predok = l.split(' ')[1]
    family.append(potomok)
    family.append(predok)
    potomok_predok[potomok] = predok

family = set(family)
print(potomok_predok)
print(family)
print(' ')

for i in family:
    i_predki = [i]
    prev = i
    while True:
        try:
            l = potomok_predok[prev]
            i_predki += [l]
            prev = l
        except KeyError:
            break
    potomok_his_ancestors[i] = i_predki

for key, value in potomok_his_ancestors.items():  
    print(f'{key}: {value}')
print(' ')

while True:
    members = input()
    member_1 = members.split(' ')[0] 
    member_2 = members.split(' ')[1]
    try:
        chain_1 = potomok_his_ancestors[member_1]
    except KeyError:
        print(f'Человека {member_1} в родословной нет')
        continue
    try:
        chain_2 = potomok_his_ancestors[member_2]
    except KeyError:
        print(f'Человека {member_2} в родословной нет')
        continue
    lca = ''
    flag = False
    for i in chain_2:
        if i in chain_1 and flag == False:
            flag = True
            lca = i
    print(lca)
