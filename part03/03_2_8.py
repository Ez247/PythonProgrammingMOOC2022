#Right-aligned

word = input("Please type in a string: ")

if len(word) < 20:
    hashes = 20 - len(word)
    print("*" * hashes + word)
