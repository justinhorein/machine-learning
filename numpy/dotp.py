#!/usr/bin/env python

import numpy as np

# Works on 2x3 * 3x2 matrix
# def dot(a, b):
#     arows, acols = a.shape
#     brows, bcols = b.shape

#     ret = np.zeros((arows, bcols), np.int32)
#     i = 0
#     j = bcols - 1
#     while i < arows:
#         for x in range(0, acols):
#             ret[i][i] += a[i][x] * b[x][i]
#             if i != j:
#                 ret[i][j] += a[i][x] * b[x][j]

#         i+=1
#         j-=1

#     return ret 

# Works on any AxN * NxB array as long as N == N	
def dot(a, b):
    arows, acols = a.shape
    brows, bcols = b.shape
    ret = np.zeros((arows, bcols), np.int32)

    for y in range(0, arows):
        for x in range(0, bcols):
            for z in range(0, brows):
                ret[y][x] += a[y][z] * b[z][x]       

    return ret



a = np.array([[1, 2, 3],[4, 5, 6], [1, 1, 1]], np.int32)
b = np.array([[7, 8, 1], [9, 10, 1], [11, 12, 1]], np.int32)
# y = np.dot(a, b)
# print(y)

print(dot(a, b))

# Result
# [[ 58  64  6]
#  [139 154 15]
#   [27, 30, 3]]