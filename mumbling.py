# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(s):
    #s = s.casefold()
    n = 0
    string = ""
    for i in range(len(s)):
        i += 1
        new_string = str(s[n]) * i
        new_string = new_string.capitalize()
        n += 1
        string = string + new_string + '-'

    string = string[:-1]
    return string

print(accum("RqaEzty"))
print(accum("abcd"))
print(accum("cwAt"))
