import datetime
from Module1.people import get_employees
from Module1.salary import calculate_salary


name1 = input('Введите мое имя!').lower()

number = int(input('Введите первое число;'))
number2 = int(input('Введите второе число:'))

if __name__ == '__main__':
    calculate_salary(number, number2)
    get_employees(name1)
    print('сегодняшняя дата:', datetime.date.today())
