limit = int(input())

items = set()
for x in range(limit):
    items.add(input().strip())

print(len(items))
