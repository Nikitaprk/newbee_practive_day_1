# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice
# versa). Leave any incidence of c untouched. Example: 'acb' --> 'bca' 'aabacbaa' --> 'bbabcabb'

def abc(string):
    for n in range(len(string)):
        if string[n] == 'a':
            string = string[:n] + 'b' + string[n + 1:]
        elif string[n] == 'b':
            string = string[:n] + 'a' + string[n + 1:]
    return string


print(abc('aaabbbccc'))
print(abc('abc'))
print(abc('aaabcccbaaa'))
print(abc('ccccc'))
print(abc('abababababababab'))
