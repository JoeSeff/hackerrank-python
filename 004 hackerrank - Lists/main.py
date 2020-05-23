if __name__ == '__main__':
    N = int(input())

    genList = list()
    for o in range(N):
        op, *args = input().split()

        if op == "insert":
            intList = list(map(int, args))
            genList.insert(intList[0], intList[1])
        elif op == "print":
            print(genList)
        elif op == "remove":
            if len(genList) > 0:
                genList.remove(int(args[0]))
        elif op == "append":
            genList.append(int(args[0]))
        elif op == "sort":
            genList.sort()
        elif op == "reverse":
            genList.reverse()
        elif op == "pop":
            if len(genList) > 0:
                genList.pop()
