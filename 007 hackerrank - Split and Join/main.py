def split_and_join(line):
    list_of_strings = line.split(" ")
    return "-".join(list_of_strings)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)