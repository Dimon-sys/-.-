#Вариант10
import csv

outfile1 = open('out.csv', 'r', encoding='UTF-8')
reader = csv.reader(outfile1, delimiter=';', quotechar='"')
outfile2 = open('out2.csv', 'w', newline='', encoding='UTF-8')
writer =  csv.writer(outfile2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
head = next(reader)
writer.writerow([head[0], head[1], head[2], head[3], head[4], head[5], head[6], 'Сумма, оплаченная за дополнительные минуты'])

for string in reader:
    extra_mins = int(string[4]) - int(string[3])
    if extra_mins > 0:
        extra_pay = extra_mins * int(string[5])
    else:
        extra_pay = 0
    writer.writerow([string[0], string[1], string[2], string[3], string[4], string[5], string[6], extra_pay])


outfile1.close()
outfile2.close()