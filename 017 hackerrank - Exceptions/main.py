limit = int(input())

for i in range(limit):
    try:
        a, b = list(map(int, input().split()))
        print(a // b)
    except ZeroDivisionError as zde:
        print("Error Code:", zde)
    except ValueError as ve:
        print("Error Code:", ve)