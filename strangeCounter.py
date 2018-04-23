#!/bin/python3

import os
import sys

def strangeCounter(t):
    initial_value = 3
    value = 3
    time = t + 1
    for iter in range(1, time):
        pair = [iter, value]
        if (value == 1):
            initial_value = initial_value * 2
            value = initial_value
        else:
            value = value - 1
        #print(pair)
        if (iter == t):
            return(pair[1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

