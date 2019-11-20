def main():
    user_input = ''
    inp = []
    student_dict = {}
    printLog = []

    while user_input != 'exit':
        user_input = str(input())
        inp = user_input.split()
        if(len(inp) == 1):
            if(inp[0] == 'print'):
                for student, grade in student_dict.items():
                    printLog.append(student + ": " + str(grade))

        if(len(inp) > 1):
            if(inp[0] == 'add'):
                if(int(inp[2]) <= 100 and inp[1] not in student_dict):
                    student_dict[str(inp[1])] = int(inp[2])
                    printLog.append("Added " + inp[1])
                else:
                    printLog.append("Failed to add " + inp[1])

            if(inp[0] == 'update'):
                if inp[1] in student_dict.keys():
                    if(int(inp[2]) <= 1000):
                        student_dict[str(inp[1])] = int(inp[2])
                        printLog.append("Updated " + inp[1] + "'s grade")
                    else:
                        printLog.append("Failed to add " + inp[1])

                elif inp[1] not in student_dict.keys():
                    printLog.append(inp[1] + " does not exist on the roster")

    for i in printLog: print(i)


if __name__ == "__main__":
    main()
