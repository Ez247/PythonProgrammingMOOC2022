#Powers of base n

number = 1

limit = int(input("Upper limit: "))
base = int(input("Base: "))

while number <= limit:
    print(number)
    number *= base
