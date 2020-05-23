def mutate_string(string, position, character):
    list_of_chars = list(string)
    list_of_chars[position] = character
    return ''.join(list_of_chars)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)