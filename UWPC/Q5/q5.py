import math
import random
import time

input = input()

array = [""]
last = ""

for letter in input:
    if (letter != last):  # abbbc
        array.append(letter)
    last = letter

result = ""
for r in array:
    result += r

print(result)
