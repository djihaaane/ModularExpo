import time
from matplotlib import pyplot as plt
import numpy as np
import random
def getRandomInRange(int start, int end):
    generator=random.getrandbits()
def naive1(b,n,m):
    start = time.perf_counter_ns()
    r = 1
    for i in range(n):
        r = r*b
    r = r%m
    stop = time.perf_counter_ns()
    period = stop - start
    return [r,period]


def naive2(b,n,m):
    start = time.perf_counter_ns()
    r = 1
    for i in range(n):
        r = (r * b)% m
    stop = time.perf_counter_ns()
    period = stop - start
    return [r, period]



def FastExponentiationIterative(b,n,m):
    r = 1
    start = time.perf_counter_ns()
    while n > 0:
        if ((n & 1)== 1):
            r=(r*b)%m
        n=n >> 1
        b=(b*b)%m
    stop = time.perf_counter_ns()
    period = stop - start
    return [r,period]

def FastExponentiationRecursive(b,n,m):
    r=1
    if n == 0:
        return 1
    if b==0:
        return 0
    # if even
    if n%2 == 0:
            r=FastExponentiationRecursive(b,n/2,m)
            r=(r*r)%m
    # if odd
    if n%2 != 0:
        r=b%m
        r=(r*FastExponentiationRecursive(b, n-1, m)%m)%m
    return (r+m)%m

def FastExponentiationRecursiveTimer(b,n,m):
    b = b-1
    start = time.perf_counter_ns()
    result = FastExponentiationRecursive(b,n,m)
    stop = time.perf_counter_ns()
    period = stop - start
    return [result,period]
    
if __name__ == '__main__':
    timesNaive1 = []
    timesNaive2 = []
    timeFastIterative = []
    timeFastRecursive = []

    for i in range (1,15):
        timesNaive1.append(0)
        timesNaive2.append(0)
        timeFastIterative.append(0)
        timeFastRecursive.append(0)
        for j in range (10):
            number = random.getrandbits(i)
            resultNaive1 = naive1((int(number)+1), (int(number)+1), (int(number)+1))
            resultNaive2 = naive2((int(number)+1), (int(number)+1), (int(number)+1))
            resultFastIterative = FastExponentiationIterative((int(number)+1), (int(number)+1), (int(number)+1))
            resultFastRecursive = FastExponentiationRecursiveTimer((int(number)+1), (int(number)+1), (int(number)+1))

            timesNaive1[i-1] += resultNaive1[1]
            timesNaive2[i-1] += resultNaive2[1]
            timeFastIterative[i-1] += resultFastIterative[1]
            timeFastRecursive[i-1] += resultFastRecursive[1]

        timesNaive1[i-1] /= 10
        timesNaive2[i-1] /= 10
        timeFastIterative[i-1] /= 10
        timeFastRecursive[i-1] /= 5
    timesNaive1 = [item for item in (timesNaive1) if item > 0]
    timesNaive2 = [item for item in (timesNaive2) if item > 0]
    timeFastIterative = [item for item in (timeFastIterative) if item > 0]
    timeFastRecursive = [item for item in (timeFastRecursive) if item > 0]

    print(timesNaive1)
    print(timesNaive2)
    print(timeFastIterative)
    print(timeFastRecursive)
    print("finished")

    plt.figure(1)
    x = [i for i in range(len(timesNaive1))]
    plt.plot(x , timesNaive1)
    plt.xticks(np.arange(0,len(timesNaive1)),rotation=90)
    plt.title("First naive method",color="green")
    plt.xlabel("Number of bits",color="red")
    plt.ylabel("Time (ns)",color="magenta")

    plt.figure(2)
    x = [i for i in range(len([item for item in (timesNaive2) if item > 0]))]
    plt.plot(x , [item for item in (timesNaive2) if item > 0])
    plt.xticks(np.arange(0, len([item for item in (timesNaive2) if item > 0])),rotation=90)
    plt.title("Second naive method",color="green")
    plt.xlabel("Number of bits",color="red")
    plt.ylabel("Time (ns)",color="magenta")

    plt.figure(3)
    x = [i for i in range(len([item for item in (timeFastIterative) if item > 0]))]
    plt.plot(x, [item for item in (timeFastIterative) if item > 0])
    plt.xticks(np.arange(0, len([item for item in (timeFastIterative) if item > 0])), rotation=90)
    plt.title("Fast (iterative method)",color="green")
    plt.xlabel("Number of bits",color="red")
    plt.ylabel("Time (ns)",color="magenta")

    plt.figure(4)
    x = [i for i in range(len([item for item in (timeFastRecursive) if item > 0]))]
    plt.plot(x, [item for item in (timeFastRecursive) if item > 0])
    plt.xticks(np.arange(0, len([item for item in (timeFastRecursive) if item > 0])), rotation=90)
    plt.title("Fast (recursive method)",color="green")
    plt.xlabel("Number of bits",color="red")
    plt.ylabel("Time (ns)",color="magenta")
    plt.show()