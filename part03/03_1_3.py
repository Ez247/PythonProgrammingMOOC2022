#Print out integer values greater than 0 but smaller than user input

number = 1

#Ask for the upper limit
limit = int(input("Upper limit: "))

#Set the condition
while number < limit:
    print(number)
    number += 1
