user_input = input()
x = user_input.split(' ')
amount = int(input())

r = int(x[0])
c = int(x[1])

matrix = []

h = 1

for i in range(r):
    a = []
    for j in range(c):
        a.append('0')
    matrix.append(a)

while h <= amount:

    e, f = map(int, input().split(' '))
    matrix[e][f] = '*'
    h += 1

l = 0

for i in range(r):

    counter = 0
    for j in range(c):

        if (i+1) < r:
            if matrix[i+1][j] == '*':
                counter+=1

            if (j+1) < c:
                if matrix[i+1][j+1] == '*':
                    counter+=1

            if (j-1) >= 0:
                if matrix[i+1][j-1] == '*':
                    counter+=1

        if (i-1) >= 0:
            if matrix[i-1][j] == '*':
                counter+=1

            if (j+1) < c:
                if matrix[i-1][j+1] == '*':
                    counter+=1

            if (j-1) >= 0:
                if matrix[i-1][j-1] == '*':
                    counter+=1

                    l = 1

        if (j+1) < c:
             if matrix[i][j+1] == '*':
                counter+=1

        if (j-1) >= 0:
            if matrix[i][j-1] == '*':
                counter+=1

        if matrix[i][j] != '*':
            matrix[i][j] = counter

        counter = 0

for r in matrix:

    print(" ".join(map(str,r)))
