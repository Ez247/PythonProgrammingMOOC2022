#Does it contain vowels

word = input("Please type in a string: ")
vowels = 'aeo'
index = 0

while index < len(word):
    vowel = vowels[index]
    if vowel in word:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
    index += 1
