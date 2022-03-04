
from application.db.people import printing_people
from application.salary import getin_many
from datetime import datetime, date, time

if __name__ == '__main__':
    name = input('введите имя')
    many = int(input('введите деньги в час'))
    printing_people(name)
    getin_many(name, many)
    print(datetime.today())



