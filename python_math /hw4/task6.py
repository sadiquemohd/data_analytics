"""
Задание 6
Напишите функцию, которая разбивает на недели с понедельника по воскресенье интервал дат между start_date и end_date.
Считайте, что входные данные всегда корректны. В ответ должны входить только полные недели.
"""
from datetime import datetime

input = ['2018-10-02', '2018-10-03', '2018-10-04', '2018-10-05', '2018-10-06', '2018-10-07', '2018-10-08', '2018-10-09',
         '2018-10-10', '2018-10-11', '2018-10-12', '2018-10-13', '2018-10-14', '2018-10-15', '2018-10-16', '2018-10-17',
         '2018-10-18', '2018-10-19', '2018-10-20', '2018-10-21', '2018-10-22', '2018-10-23', '2018-10-24', '2018-10-25',
         '2018-10-26', '2018-10-27', '2018-10-28', '2018-10-29', '2018-10-30', '2018-10-31', '2018-11-01', '2018-11-02',
         '2018-11-03', '2018-11-04', '2018-11-05', '2018-11-06', '2018-11-07', '2018-11-08', '2018-11-09', '2018-11-10',
         '2018-11-11', '2018-11-12', '2018-11-13', '2018-11-14', '2018-11-15', '2018-11-16', '2018-11-17', '2018-11-18',
         '2018-11-19', '2018-11-20', '2018-11-21', '2018-11-22', '2018-11-23', '2018-11-24', '2018-11-25', '2018-11-26',
         '2018-11-27', '2018-11-28', '2018-11-29', '2018-11-30', '2018-12-01', '2018-12-02', '2018-12-03', '2018-12-04',
         '2018-12-05', '2018-12-06', '2018-12-07', '2018-12-08', '2018-12-09', '2018-12-10']

def weekSpliter(stream):
    weeks = 0
    days = 0
    result = {}
    while days < len(stream):
        key = 'week{}'.format(weeks)
        while True:
            if days >= len(stream):
                return doFullWeek(result, weeks)
            temp = datetime.strptime(stream[days], '%Y-%m-%d')
            if not (key in result):
                result[key] = []
            result[key].append(temp.strftime('%Y-%m-%d'))
            days += 1
            if temp.strftime('%w') == '0':
                break
        weeks += 1
    return doFullWeek(result, weeks)


def doFullWeek(map, weeks):
    if len(map['week0']) != 7:
        map.pop('week0')

    if len(map['week{}'.format(weeks)]) != 7:
        map.pop('week{}'.format(weeks))

    return map


print(weekSpliter(input))

