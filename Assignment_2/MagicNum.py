#we definitely know that 30 is the starting number, so lets start with 30

def loop(n):
    counter = 0
    i = 30
    while(counter < n):
        if(len(checkPrimes(i)) >= 3):
            print(i)
            counter+=1
        i+=1

def checkPrimes(n):
    x=2
    primes = []
    finalprimes = []
    while(x <= n):
        if(n%x == 0):
            primes.append(x)
            n//=x
        if(n%x != 0):
            x+=1

    [finalprimes.append(x) for x in primes if x not in finalprimes]

    return finalprimes

user_input = int(input())
loop(user_input)
