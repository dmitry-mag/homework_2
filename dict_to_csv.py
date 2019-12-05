"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    persons = [{'name': 'John', 'age': 25, 'job': 'taxi driver'},
               {'name': 'Alice', 'age': 30, 'job': 'painter'},
               {'name': 'Max', 'age': 36, 'job': 'photographer'},
               {'name': 'Julia', 'age': 33, 'job': 'web developer'},
               {'name': 'Tiffany', 'age': 29, 'job': 'cook'},
              ]

    with open('persons.csv', 'w', encoding='utf-8', newline='') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for person in persons:
            writer.writerow(person)

if __name__ == "__main__":
    main()
