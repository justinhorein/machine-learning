#!/usr/bin/env python

import numpy as np

# Works on 2x3 * 3x2 matrix
def dot(a, b):
    arows, acols = a.shape
    brows, bcols = b.shape

    ret = np.zeros((arows, bcols), np.int32)
    i = 0
    j = bcols - 1
    while i < arows:
        for x in range(0, acols):
            ret[i][i] += a[i][x] * b[x][i]
            if i != j:
                ret[i][j] += a[i][x] * b[x][j]

        i+=1
        j-=1

    return ret 
	

a = np.array([[1, 2, 3],[4, 5, 6]], np.int32)
b = np.array([[7, 8], [9, 10], [11, 12]], np.int32)

# y = np.dot(a, b)
# print(y)

print(dot(a, b))

