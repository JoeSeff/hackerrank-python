import re

limit = int(input())
for n in range(limit):
    pattern = input()
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
