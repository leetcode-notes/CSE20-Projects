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

def getMaxMode(lis):
    mode = 0
    newlis = [i//10 * 10 for i in lis]
    counter = 0
    for i in newlis:
        curr = newlis.count(i)
        if(curr>counter):
            counter = curr
            mode = i

    return int(counter)

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

    lis = [i//10 * 10 for i in lis]
    lis.sort()

    mode = getMode(lis)/10
    maxDiv = getMax(lis)//10 * 10
    max = 0
    maxMode = getMaxMode(lis)

    for i in lis:
        if i%maxDiv<10 and i%maxDiv>=0:
            max+=1

    for i in range(0, maxDiv+10, 10):
        if(i == 0 and maxDiv >= 100):
            print("  ", end="")
        if(i == 0 and maxDiv < 100):
            print(" ", end="")
        if(10<=i<100 and maxDiv >= 100):
            print(" ", end="")

        print(i, end=" ")

        counter = lis.count(i)
        numPounds = int((counter/maxMode)*16)

        for i in range(numPounds):
            print("#", end="")

        for i in range(16 - numPounds):
            print(" ", end="")

        print("", counter)

if __name__ == '__main__':
    main()
