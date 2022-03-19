from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
import re

# находит ФИО
# использую сайт https://regex101.com/ для составления паттерна
pattern = '^([А-Я]+[а-я]*)+[ {1}|,{1}]+([А-Я]+[а-я]*)+[ {1}|,{1}]+([А-Я]+[а-я]*)'
pattern_telefon = '(7|8)[ |(]{0,2}(\d{3})[ |)|-]{0,2}(\d{0,7})[-?]?(\d{0,4})[-?]?(\d{0,2})[ |(]{0,2}(доб)?[\.| ]{0,2}(\d{0,4})'

# ФИО ищем
n = 1
print(contacts_list[n])
print(','.join(contacts_list[n]))
list1 = re.match(pattern, ','.join(contacts_list[n]))
print(list1)
print(list1.group(1))
print(list1.group(2))
print(list1.group(3))
contacts_list[n][0] = list1.group(1)
contacts_list[n][1] = list1.group(2)
contacts_list[n][2] = list1.group(3)
print(contacts_list[1])

#ищем телефон
telefon = re.search(pattern_telefon, ','.join(contacts_list[n]))
print(telefon)
if telefon != None:
  contacts_list[n][5] = f'+{telefon.group(1)}({telefon.group(2)}){telefon.group(3)}{telefon.group(4)}{telefon.group(5)} {telefon.group(6)}.{telefon.group(7)}'
  print(contacts_list[n][5])
  contacts_list[n][5] = contacts_list[n][5].replace('None.', '')
print(contacts_list[n][5])



#word_list = re.findall(pattern, contacts_list)
#print(type(word_list))

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)