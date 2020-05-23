#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    word_list = list(s.split(' '))
    for index, word in enumerate(word_list):
        if word != '':
            w = list(word)
            w[0] = w[0].upper()
            word_list[index] = ''.join(w)
    return ' '.join(word_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
