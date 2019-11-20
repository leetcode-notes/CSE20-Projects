user_input = ''
def checkLongestNum(inp):
    assert type(inp) == str
    new = inp.split('0')
    max = 0
    for i in new:
        if len(i)>max:
            max = len(i)
    return max
    #splits the str into subchars
    #for loop that checks the longest streak of 1s
def main():
    user_input = str(input())
    print(checkLongestNum(user_input))

if __name__ == "__main__":
    main()
