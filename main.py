import datetime
from people import get_employees
from salary import calculate_salary


name1 = input('Введите мое имя!').lower()

number = int(input('Введите первое число;'))
number2 = int(input('Введите второе число:'))

if __name__ == '__main__':
    calculate_salary(number, number2)
    get_employees(name1)
    print('сегодняшняя дата:', datetime.date.today())
