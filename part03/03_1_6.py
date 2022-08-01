#The sum of consecutive numbers, version 1.

number = 1
calc = 0

limit = int(input("Limit: "))

while calc < limit:
    calc += number
    number += 1
print(calc)
