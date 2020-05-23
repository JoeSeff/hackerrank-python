if __name__ == '__main__':

    physicsDict = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        physicsDict[name] = score

    scoresSet = sorted(set(physicsDict.values()))
    secondLowest = scoresSet[1]

    namesList = list()
    for i, j in physicsDict.items():
        if j == secondLowest:
            namesList.append(i)

    for x in sorted(namesList):
        print(x)