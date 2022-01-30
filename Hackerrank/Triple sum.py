# https://www.hackerrank.com/challenges/triple-sum/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# def binary_search(ara, key):
#     left, right = 0, len(ara) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if ara[mid] == key:
#             if mid == right:
#                 return right + 1
#             if ara[mid + 1] > key: 
#                 return mid + 1
#             if ara[mid + 1] == key:
#                 left = mid + 1
#         elif ara[mid] < key:
#             left = mid + 1
#         else:
#             right = mid -1

#     return left

from bisect import bisect_right

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(set(a))  # O(n)
    b = list(set(b))
    c = list(set(c))
    a.sort()  # O(n log n)
    b.sort()
    c.sort()

    count = 0
    for q in b:  #O(n)
        # n1 = number of items in a, <= q
        n1 = bisect_right(a, q)  # O(log n)

        # n2 = number of items in c, <= q
        n2 = bisect_right(c, q)
        
        count += n1 *  n2 

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
