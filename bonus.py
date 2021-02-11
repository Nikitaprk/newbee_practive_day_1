# It's bonus time in the big city! The fatcats are rubbing their paws in anticipation...
# but who is going to make the most money?
# Build birthdate function that takes in two arguments (salary, bonus).
# Salary will be an integer, and bonus birthdate boolean.
# If bonus is true, the salary should be multiplied by 10. If bonus is false,
# the fatcat did not make enough money and must receive only his stated salary.


def bonus_time(salary, bonus):
    if bonus:
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)


print(bonus_time(10000, True))
print(bonus_time(25000, True))
print(bonus_time(10000, False))
print(bonus_time(60000, False))
