def average(array):
    sum_set = set(array)
    sum = 0
    for item in sum_set:
        sum += item
    return sum/len(sum_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
