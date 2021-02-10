# A person's Life Path Number is calculated by adding each individual number in that person's date of birth,
# untill it is reduced to a single digit number.
# For example, Albert Einstein's birthday is March 14, 1879.
# The calculation of his Life Path Number would look like this:
# year: 1 + 8 + 7 + 9 = 25; 2 + 5 = 7
# month: 0 + 3 = 3
# day: 1 + 4 = 5
# final result: 7 + 3 + 5 = 15; 1 + 5 = 6


def life_path_number(birthdate):
    birthdate = birthdate.split('-')
    sum = []
    for i in range(2):
        if len(birthdate[i]) > 2:
            sum = int(birthdate[i][0]) + int(birthdate[i][1]) + int(birthdate[i][2]) + int(birthdate[i][3])
            if sum > 9:
                sum = str(sum)
                sum = int(sum[0]) + int(sum[1])
        else:
            sum = sum + int(birthdate[1][0]) + int(birthdate[1][1])
            sum = sum + int(birthdate[2][0]) + int(birthdate[2][1])
            if sum > 9:
                sum = str(sum)
                sum = int(sum[0]) + int(sum[1])
                if sum > 9:
                    sum = str(sum)
                    sum = int(sum[0]) + int(sum[1])
            return sum


# so f***ing quick'n'dirty :))


print(life_path_number("2470-05-28 "))
print(life_path_number("1971-06-28"))




