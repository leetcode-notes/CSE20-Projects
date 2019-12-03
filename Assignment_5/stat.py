import unittest

def getMean(lis):
    total = 0
    for i in range(len(lis)):
        total += lis[i]

    mean = round(total/len(lis), 2)
    mean = "%0.2f" % mean
    return mean

def getMode(lis):
    mode = 0
    newlis = [i//10 * 10 for i in lis]
    counter = 0
    for i in newlis:
        curr = newlis.count(i)
        if(curr>counter):
            counter = curr
            mode = i

    return int(mode)


def getMedian(lis):
    lis.sort()
    median = 0

    if(len(lis) % 2 == 0):
        median = (lis[int(len(lis)/2)]+lis[int(len(lis)/2 -1)])/2
    if(len(lis) % 2 != 0):
        median = (lis[int(len(lis)//2)])

    median = round(median, 2)
    median = "%0.2f" % median
    return median

def getMin(lis):
    min = lis[0]
    for i in range(len(lis)):
        if lis[i] < min:
            min = lis[i]

    #still try to implement divide and conquer
    return int(min)

def getMax(lis):
    max = lis[0]
    for i in range(len(lis)):
        if lis[i] > max:
            max = lis[i]

    #still try to implement divide and conquer
    return int(max)

def main():
    lis = input().split(',')
    lis = [float(i) for i in lis]

    print("Mean   ", getMean(lis))
    print("Median ", getMedian(lis))
    print("Mode   ", getMode(lis))
    print("Minimum", getMin(lis))
    print("Maximum", getMax(lis))




if __name__ == '__main__':
    main()
