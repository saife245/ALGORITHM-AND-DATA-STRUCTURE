import numpy as np
import random
import time 

n= int(input())
np.random.seed(0)
A = np.random.randint(0, 10, size=(n,n))
B = np.random.randint(0, 10, size=(n,n))
result = np.zeros((n,n))
print(A)
print(B)

start_time = time.time()

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)

print("--- %s seconds ---" % (time.time() - start_time))
