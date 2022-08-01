#Countdown Timer when given an input

print("Are you ready?")

#Ask the user for a number
number = int(input("Please type in a number: "))

while number > 0:
    print(number)
    number -= 1

print("Now!")
