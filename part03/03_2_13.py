#Find the first substring
word = input("Please type in a word: ")
char = input("Please type in character: ")

index = word.find(char)

if index != 1 and len(word) >= 3:
    print(word[index:index+3])
