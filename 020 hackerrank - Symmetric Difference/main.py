size_set_a = int(input())
set_a = set(list(map(int, input().split(' '))))
size_set_b = int(input())
set_b = set(list(map(int, input().split(' '))))

union_set = set_a | set_b
intersection_set = set_a & set_b
symmetric_difference_list = list(union_set.difference(intersection_set))

for item in sorted(symmetric_difference_list):
    print(item)
