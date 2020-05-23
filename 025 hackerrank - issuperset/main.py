def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


superset = set(list(map(int, input().split(" "))))

limit = int(input())
is_superset = True
for x in range(limit):
    line = input().strip()

    if ' ' in line:
        subset = set(list(map(int, line.split(" "))))
    else:
        subset = [int(line)]

    if not (len(superset) > len(subset) and superset.issuperset(subset)):
        is_superset = False
        break

print(is_superset)
