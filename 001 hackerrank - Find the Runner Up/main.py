if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scoresList = sorted(set(arr))
    print(scoresList[-2])
