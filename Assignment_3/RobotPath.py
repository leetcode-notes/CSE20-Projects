ref = ['U', 'L', 'R', 'D']

def theRoundTrip(inp):
    directions = inp.split(',')
    x = 0
    y = 0

    try:
        check = all(i in ref for i in directions)
        assert(check)
        for dir in directions:
            if dir == 'L':
                x -=1
            if dir == 'R':
                x +=1
            if dir == 'D':
                y -=1
            if dir == 'U':
                y +=1

        if x == 0 and y == 0:
            return True
        return False

    except AssertionError:
        return 0

user_input = str(input())

if(type(theRoundTrip(user_input)) == int):
    print("bad input")
if(type(theRoundTrip(user_input)) == bool):
    print(theRoundTrip(user_input))
