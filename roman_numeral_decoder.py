# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.


def solution(roman):
    numbers = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)
    index = 1
    list = []

    if len(roman) == 1:
        list.append(numbers.get(roman))


    elif len(roman) <= 2:  # исключение, если чисел меньше или равно 2
        if numbers.get(roman[0]) >= numbers.get(roman[1]):
            list.append(numbers.get(roman[0]) + numbers.get(roman[1]))
        else:
            list.append(numbers.get(roman[1]) - numbers.get(roman[0]))
    else:
        list.append(numbers.get(roman[0]))
        for i in range(len(roman) - 2):  # количество итераций равняется числу на 2 меньшему длинне слова
            if index < len(roman):
                if numbers.get(roman[index]) >= numbers.get(roman[index + 1]):
                    list.append(numbers.get(roman[index]))
                    index += 1
                    if index == len(roman) - 1:
                        list.append(numbers.get(roman[-1]))
                else:
                    list.append(numbers.get(roman[index + 1]) - numbers.get(roman[index]))
                    index += 2

    return sum(list)


print(solution('I'))
print(solution('XXI'))  # 21
print(solution('MDCLXVI'))  # 1666
print(solution('MMVIII'))  # 2008
print(solution('MCMXC'))  # 1990
print(solution('MMMCMXCIX'))  # 3999

# первое число записываем всегда, 2 сравниваем с 3, если 2>=3, пишем 2, если нет, то пишем разницу между 3 и 2, и идем
# 4 числу, сравниваем его с последующим и так до конца строки
'''
numbers = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)
index = 1
list = []
list.append(numbers.get("M"))
print(list)
'''
