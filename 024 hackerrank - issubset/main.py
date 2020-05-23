limit = int(input())

for x in range(limit):
    a = input() #useless
    set_a = set(list(map(int, input().split(" "))))
    b = input() #useless
    set_b = set(list(map(int, input().split(" "))))

    print(set_a.issubset(set_b))
