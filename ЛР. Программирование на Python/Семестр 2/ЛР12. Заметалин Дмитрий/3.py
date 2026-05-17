import faker
import random
from re import *

'''
faker = faker.Faker('ru_Ru')
outfile = open('3.txt', 'w', newline='', encoding='UTF-8')
for i in range(20):
    initials = f"{faker.last_name()} {faker.name()[0]}.{faker.middle_name()[0]}."
    outfile.write(f"{initials} - ${random.randint(5000, 12000)}\n")

outfile.close()
'''

pattern = compile(r'([А-ЯЁ][а-яё]+) [А-ЯЁ]\.[А-ЯЁ]\. - \$(\d+)')

with open('3.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        match = pattern.match(line)
        surname = match.group(1)
        salary = int(match.group(2))
        if salary > 9000:
            print(surname)