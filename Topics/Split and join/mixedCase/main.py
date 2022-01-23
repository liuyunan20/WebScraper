import string

words = input().split()
camel_part = string.capwords(" ".join(words[1:]))
words = [words[0]] + camel_part.split()
print("".join(words))
