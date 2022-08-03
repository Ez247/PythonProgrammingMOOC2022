#A framed word

word = input("Word: ")

for i in range(3):
    for j in range(30):
        if i == 0 or i == 2 or j == 0 or j == 29:
            print("*", end="")
        else:
            print(" ", end="")
    print()
