# Move every letter in the provided string forward 10 letters through the alphabet.
# If it goes past 'z', start again at 'a'.
# Input will be a string with length > 0.

def move_ten(st):
    alphabet = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w',
        'x',
        'y', 'z')  # 26 letters
    string = ''
    for i in range(len(st)):
        for letter in alphabet:
            if letter in st[i]:
                index = alphabet.index(letter)
                index = index + 10
                if index == 26:  # exception for 'q' letter which has 26 index and its out of range
                    string = string + str('a')
                    break
                elif index > 26:
                    index = index % 26
                else:
                    string = string + str(alphabet[index])
                    break
                string = string + str(alphabet[index])
    return string


print(move_ten("qqq"))
print(move_ten("exampletesthere"))
print(move_ten("returnofthespacecamel"))
print(move_ten("bringonthebootcamp"))


# идем по букве в строке, ищем соответствие со строкой алфавита, прибавляем к индексу 9, если больше 26, то берем
# остаток от деления, добавляем в новую строку символ, который нашли