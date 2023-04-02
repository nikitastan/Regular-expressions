# This is a sample Python script.
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re


def fio_change(row):
    fio = ' '.join(row[0:3]).strip().split(' ')
    if len(fio) < 3:
        fio += ['']
    row[:3] = fio[:3]
    return row[:7]


def phone_change(row):
    result_phone = re.sub(
        r"(\+7|8)\W*(\d{3})\W*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})",
        r"+7(\2)\3-\4-\5", row[5])
    row[5] = re.sub(r"\(*доб.\s*(\d{4})\)*", r"доб.\1", result_phone)
    return row


def merge_rows(list1, list2):
    new_list = []
    for i in range(len(list2)):
        if list2[i] == '':
            new_list.append(list1[i])
        else:
            new_list.append(list2[i])
    return new_list


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

## 1. Выполните пункты 1-3 задания.
phone_dict = {}
for row in contacts_list:
    row = fio_change(row)
    row = phone_change(row)
    first_last_names = ' '.join(row[0:2])
    if first_last_names not in phone_dict:
        phone_dict[first_last_names] = row
    else:
        phone_dict[first_last_names] = merge_rows(phone_dict[first_last_names], row)
contacts_list_new = list(phone_dict.values())

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8',newline='') as f:
    datawriter = csv.writer(f, delimiter=';')
    datawriter.writerows(contacts_list_new)
