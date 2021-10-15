import os

def main():
    # print(isUniqueChar("abc"))
    # printUniqueChar("the quick brown fox jumped over the lazy sheep dog")
    # print(checkPerm("jiujitsu ", "us tijuij"))
    # reverseString("elguezabal")
    # replaceChars("this is a string that I want to change", 'a', "Fizz")
    # print("Hello, " + os.getlogin())
    fizzBuzz()

""" An algorithm that determines if all characters in a string are unique.
     returns true or false"""

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

""" Check to see if string a is a permutation of string b """
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

""" Reverse a given string """
def reverseString(string):
    # stringList = []
    # for x in string:
    #     stringList.append(x)
    
    # reversedStringList = []
    # counter = len(string) - 1
    # while counter >= 0:
    #     reversedStringList.append(stringList[counter])
    #     counter -= 1
    
    # reversedString = ''.join(reversedStringList)

    str = ""
    for x in string:
        str = x + str
    print(str)

" Replace a chosen character with a given character"
def replaceChars(string, replaceChar, replaceWith):

    # replacedString = string.replace(replaceChar, replaceWith)
    # print(replacedString)

    replaceCharLoc = []

    # Starting at index 0 find all the indicies where the replace char is in original string
    index = 0
    for x in string:
        if x == replaceChar:
            replaceCharLoc.append(index)
        index += 1
    
    # Turn string into a list (cause strings are immutable)
    newString = list(string)

    # for every index in the replace array, go in at that index in the new string and replace 
    # it with the replace char
    for x in replaceCharLoc:
        newString[x] = replaceWith
    
    # join the string converted to a list back into a string
    newString = "".join(newString)

    print(newString)

'''Trying the classic fizz buzz problem'''
def fizzBuzz():

    for x in range(100):
        # have to do this or else will print 0 - 99
        num = x + 1

        # remember you have to do check for 3 and 5 first or else it will get skipped afterwards
        if (((num % 3) == 0) and ((num % 5) == 0)):
            print("FizzBuzz")
        elif ((num % 3) == 0):
            print("Fizz")
        elif ((num % 5) == 0):
            print("Buzz")
        else:
            print(num)

    




            



main()