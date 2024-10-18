import Homework1_Code as hwc
import Homework1_Code_Revamp as hwcr
import random as rnd
from time import time
import matplotlib.pyplot as plt
import numpy as np


def random_arr(n): #prints a square matrix of size 2^n, with real values between -100 and 100.
    a = []
    for i in range(0,2**(2*n)):
        a.append(rnd.randint(-100,100))
    return a

def time_measure(fnct, a, b): #measures the execution time for functions with parameters a and b, in this case, the product functions.
    t0 = time()
    fnct(a,b)
    t1 = time()
    return t1-t0

A = []
B = []

for s in range(7, 11): #filling A and B with random matrices of sizes 2^0 to 2^8, just this process takes around 0.7 seconds for each of them.
    A.append(np.array(random_arr(s)).reshape(2**s,2**s))
    B.append(np.array(random_arr(s)).reshape(2**s,2**s))

prod_times = []
strassen_times = []
strassen3_times = []
for s in range(0, 4):
    prod_times.append(time_measure(hwcr.prodnp, A[s], B[s]))
    strassen_times.append(time_measure(hwcr.strassennp, A[s], B[s]))
    #strassen3_times.append(time_measure(hwcr.strassen3, A[s], B[s]))


#Plotting the results with mathplotlib
plt.figure(figsize=(10, 6))
plt.plot(list(range(7, 11)), prod_times, label='Usual Product', marker='o')
plt.plot(list(range(7, 11)), strassen_times, label="Strassen's Product", marker='x')
plt.xlabel('Matrix Size (2^N)')
plt.ylabel('Execution Time (Seconds)')
plt.title('Performance Comparison for 0<=N<=7')
plt.legend()
plt.grid(True)
plt.show()