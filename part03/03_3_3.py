#Factorial

from re import I


while True:
    num = int(input("Please type in a number: "))
    fact = 1
    if num <= 0:
        break
    else:
        for i in range(1, num+1):
            fact = fact * i
        print(f"The factorial of the number {num} is {fact}")

print("Thanks and bye! ")
