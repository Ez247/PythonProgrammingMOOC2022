#Substrings, part1

word = input("Please type in a string: ")
char = 1

while char <= len(word):
    print(word[:char])
    char += 1
