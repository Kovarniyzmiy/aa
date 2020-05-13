import csv

with open('yakut_short.txt', 'r', encoding='utf-8') as f:
    file = f.read()
# print(file)

file = file.split('список УСЛОВНЫХ СОКРАЩЕНИЙ')[1]

file = file.replace('­\n', '').replace('-\n', '')

file = file.split('.\n')
with open('lng.csv', 'w', newline='', encoding='utf-8') as fl:
    writer = csv.writer(fl)
    for i in file:
        i = i.split(';')
        if len(i) >= 3:
            writer.writerow((i[0], i[1], i[2]))

# print(file)
