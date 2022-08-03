#First letters of word

sentence = input("Please type in a sentence: ")
word = sentence.split()

for char in word:
    print(char[0])
