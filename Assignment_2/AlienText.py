def checkPunctuation(sentence):
    #checks if punctuation is correct
    if(sentence.endswith('!')):
        return False
    return True

def checkAlienLang(sentence):
    assert type(sentence) == str
    minimize = sentence.split()
    new_minimize = []

    for i in minimize:
        x=i.lower()
        if(checkPunctuation(i)):

            if(i.endswith(',')):
                x = i.replace(i, i[: len(i)-1])

            if(i.endswith('?')):
                x = i.replace(i, i[: len(i)-1])

            if(i.endswith('.')):
                x = i.replace(i, i[: len(i)-1])

            new_minimize.append(x)

        if(checkPunctuation(i) == False):
            return False

    for i in new_minimize:
        if(i.isdigit() == True):
            if (i[0] == '0'):
                continue
            else:
                return False
        if(i.isalpha() == True):
            if (i[::-1] == i):
                continue
            else:
                return False
        else:
            return False

    return True

inp = str(input())
print(checkAlienLang(inp))
