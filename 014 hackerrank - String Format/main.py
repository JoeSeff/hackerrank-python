def print_formatted(number):
    width = len(str("{0:b}".format(number)))
    for num in range(1, number+1):
        for base in 'doXb':
            print('{0:{base}}'.format(num, base=base).rjust(width)+' ', end='')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    #print("{0:b}".format(n))
    #print(str(bin(n)))