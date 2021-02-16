str ="01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"


def first(str):
    str = str.replace(' ', '')
    str = str.split(',')  # сплитим по запятым, получается список из 3 значений
    first_nums = []
    for n in range(len(str)):  # цикл для выделения 1 значений из всего списка
        x = str[n].replace('|', ' ')  # присваиваем значение x n-нному элементу списка, тем самым делаем еще один список
        x = x.split(' ')
        first_nums.append(int(x[0]))
    return first_nums


def second(str):
    str = str.replace(' ', '')
    str = str.split(',')  # сплитим по запятым, получается список из 3 значений
    second_nums = []
    for n in range(len(str)):  # цикл для выделения 1 значений из всего списка
        x = str[n].replace('|', ' ')  # присваиваем значение x n-нному элементу списка, тем самым делаем еще один список
        x = x.split(' ')
        second_nums.append(int(x[1]))
    return second_nums


def third (str):
    str = str.replace(' ', '')
    str = str.split(',')  # сплитим по запятым, получается список из 3 значений
    third_nums = []
    for n in range(len(str)):  # цикл для выделения 1 значений из всего списка
        x = str[n].replace('|', ' ')  # присваиваем значение x n-нному элементу списка, тем самым делаем еще один список
        x = x.split(' ')
        third_nums.append(int(x[2]))
    return third_nums



print(first(str))
print(second(str))
print(third(str))