#Вариант10
import csv
import faker
import random

fake = faker.Faker('ru_Ru')
outfile = open('out.csv', 'w', newline='', encoding='UTF-8')
outdata = csv.writer(outfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
outdata.writerow(['№', 'ФИО', 'Номер телефона', 'Количество минут, оплаченных абонентом', 'Количество минут, которые наговорил абонент', 'Стоимость дополнительной минуты', 'Адрес'])
for i in range(1, 10001):
    outdata.writerow([i, fake.name(), fake.phone_number(), random.randint(1, 500), random.randint(1, 600), random.randint(1, 50), fake.address()])

outfile.close()
