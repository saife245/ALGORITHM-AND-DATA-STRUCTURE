import random
import numpy as np
import time

n = int(input())
np.random.seed(0)
matrix1 = np.random.randint(0, 10, size=(n,n))
matrix2 = np.random.randint(0, 10, size=(n,n))

print(matrix1)
print(matrix2)

start_time = time.time()

def splitter(matrix):
    row, col = matrix.shape
    return matrix[:row//2 ,:(col//2)], matrix[:row//2, col//2:], matrix[row//2:, :col//2], matrix[row//2:, col//2:]

def strassens(x,y):
    l = len(x)

    if l == 1:
        return x*y
    
    x11, x12, x21, x22 = splitter(x)
    y11, y12, y21, y22 = splitter(y)

    p1 = strassens(x11+x22, y11+y22)
    p2 = strassens(x21+x22, y11)
    p3 = strassens(x11, y12-y22)
    p4 = strassens(x22, y21-y11)
    p5 = strassens(x11+x12, y22)
    p6 = strassens(x21-x11, y11+y12)
    p7 = strassens(x12-x22, y21+y22)

    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 +p4
    c22 = p1 + p3 -p2 + p6
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c
print("The result is :")
print(strassens(matrix1,matrix2))

print("--- %s seconds ---" % (time.time() - start_time))

