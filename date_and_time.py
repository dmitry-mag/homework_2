"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    print(f'Yesterday is {(today - timedelta(days=1)).strftime("%d.%m.%Y")}')
    print(f'Today is {today.strftime("%d.%m.%Y")}')
    print(f'One month ago is {(today - timedelta(days=30)).strftime("%d.%m.%Y")}')
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
    
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
