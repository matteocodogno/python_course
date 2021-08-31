import math
import os
import random
import re
import sys

# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])
n = 7
m = 3
# m = int(first_multiple_input[1])

matrix = ['Tsi', 'h%x', 'i #', 'sM ', '%a ', '#t%', 'ir!']
# matrix = []

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

lst = list(zip(*matrix))

encoded_str = ''
for t in lst:
    encoded_str += ''.join(t)

decoded_str = re.sub(r'([^\w\d]+)(?=\w)', ' ', encoded_str)
print(decoded_str)
