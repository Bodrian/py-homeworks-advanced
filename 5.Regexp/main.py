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
pattern = '^([А-Я]+[а-я]*)+[ {1}|,{1}]+([А-Я]+[а-я]*)+[ {1}|,{1}]+([А-Я]+[а-я]*)'
print(contacts_list[1])
print(','.join(contacts_list[1]))
list1 = re.match(pattern, ','.join(contacts_list[1]))
print(list1)
print(list1.group(3))
#word_list = re.findall(pattern, contacts_list)
#print(type(word_list))

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)