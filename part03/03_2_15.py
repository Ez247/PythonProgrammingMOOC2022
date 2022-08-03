#The second occurrence

from re import sub


word = input("Please type in a string: ")
string = input("Please type in a substring: ")

substring = string

if True:
    index = word.find(substring)
    if index >= 0:
        if substring != 2:
            count = word.find(substring[:])
            print(f"The occurrence of the substring is at index {count}")
        else:
            print("The substring does not occure twice in the string")
