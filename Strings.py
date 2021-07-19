def main():
    # print(isUniqueChar(""))
    # printUniqueChar("the quick brown fox jumped over the lazy sheep dog")
    # print(checkPerm("jiujitsu ", "us tijuij"))
    # reverseString("hello")
    replaceChars("this is a string that I want to change", ' ', "%20")

def isUniqueChar(string):
    count = 0
    charList = []
    for x in string:
        for y in charList:
            if x == y:
                count += 1
        if count == 0:
            charList.append(x)
        else:
            return False
    return True


def printUniqueChar(string):
    count = 0
    charList = []
    for x in string:
        for y in charList:
            if x == y:
                count += 1
        if count == 0:
            charList.append(x)
        else:
            count = 0
    print(charList)

def checkPerm(a , b):
    if len(a) != len(b):
        return False
    
    aList = []
    for x in a:
        aList.append(x)
    aList.sort()

    bList = []
    for x in b:
        bList.append(x)
    bList.sort()

    if aList == bList:
        return True
    else:
        return False 

def reverseString(string):
    stringList = []
    for x in string:
        stringList.append(x)
    
    reversedStringList = []
    counter = len(string) - 1
    while counter >= 0:
        reversedStringList.append(stringList[counter])
        counter -= 1
    
    reversedString = ''.join(reversedStringList)
    print(reversedString)

def replaceChars(string, replaceChar, replaceWith):
    replacedString = string.replace(replaceChar, replaceWith)
    print(replacedString)


    




            



main()