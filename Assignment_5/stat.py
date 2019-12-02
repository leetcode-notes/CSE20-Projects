import unittest

lis = []

def getMean(lis):
    total = 0
    for i in lis:
        total += i

    return total/len(lis)

def getMode():
    '''
    maybe we can use split??
    alternative is to just mark one number and see which is the greatest
    keep taking out numbers until one has taken out the most
    '''
    pass

def getMedian():
    '''
    order the entire list
    then find the middle
    if the middle is even, then add two numbers together then divide by two
    '''
    pass

def getMin(lis, i):
    min = lis[0]
    '''
    if lis[i] <= min:
        min = lis[i]
    else:
        getMin(lis, i+ len(lis)/2))
    '''

    return min

def getMax():
    max = lis[0]

    return max

def main():
    lis = input().split()
    print("Mean:", getMean(lis))
    print("Median:", getMedian(lis))
    print("Mode:", getMode(lis))
    print("Maximum:", getMax(lis))
    print("Minimum:", getMin(lis))

if __name__ == '__main__':
    main()
