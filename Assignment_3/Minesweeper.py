def printGrid(grid):
    for i in grid:
        print(" ".join(map(str,i)))

def changeSurroundings(grid):
    row = len(grid)
    col = len(grid[0])
    l = 0
    for i in range(row):
        count = 0
        for j in range(col):
            if (i+1) < row:
                if grid[i+1][j] == '*':
                    count+=1

                if (j+1) < col:
                    if grid[i+1][j+1] == '*':
                        count+=1

                if (j-1) >= 0:
                    if grid[i+1][j-1] == '*':
                        count+=1

            if (i-1) >= 0:
                if grid[i-1][j] == '*':
                    count+=1

                if (j+1) < col:
                    if grid[i-1][j+1] == '*':
                        count+=1

                if (j-1) >= 0:
                    if grid[i-1][j-1] == '*':
                        count+=1
                        l = 1

            if (j+1) < col:
                 if grid[i][j+1] == '*':
                    count+=1

            if (j-1) >= 0:
                if grid[i][j-1] == '*':
                    count+=1

            if grid[i][j] != '*':
                grid[i][j] = count

            count = 0



    return grid

def main():
    user_input = str(input())
    dimensions = user_input.split()
    dimensions = [int(i) for i in dimensions]
    row = dimensions[0]
    col = dimensions[1]
    grid = [[0 for x in range(col)] for y in range(row)]

    numBombs = int(input())

    for i in range(numBombs):

        bombLoc = str(input())
        bombCoord = bombLoc.split()
        bombCoord = [int(i) for i in bombCoord]
        x = bombCoord[0]
        y = bombCoord[1]

        grid[x][y] = '*'
        changeSurroundings(grid)

    printGrid(grid)


if __name__ == "__main__":
    main()
