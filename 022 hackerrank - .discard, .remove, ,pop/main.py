set_size = int(input()) #useless
main_set = set(list(map(int, input().split(" "))))
op_count = int(input())

for x in range(op_count):
    try:
        # do something
        op_string = input()
        if 'pop' in op_string:
            main_set.pop()
        elif 'discard' in op_string:
            index = int(op_string.split(" ")[1])
            main_set.discard(index)
        elif 'remove' in op_string:
            index = int(op_string.split(" ")[1])
            main_set.remove(index)
    except:
        print('', end='')

sum = 0
for y in main_set:
    sum += y
print(sum)
