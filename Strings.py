import os

def main():
    # print(isUniqueChar("abc"))
    # printUniqueChar("the quick brown fox jumped over the lazy sheep dog")
    # print(checkPerm("jiujitsu ", "us tijuij"))
    # reverseString("elguezabal")
    # replaceChars("this is a string that I want to change", 'a', "Fizz")
    # print("Hello, " + os.getlogin())
    # fizzBuzz()
    # print(palindromePermutation("racecar!"))
   print(oneAway("pales", "pales"))

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

""" Given a string, check to see if it is a palindrome of a permutation"""
def palindromePermutation(string):

    # Make the string into list 
    stringList = []
    for x in string:
        stringList.append(x)

    # Sort to make it easier to work with
    stringList.sort()

    # count number of times a character appears in the string
    charCounter = []
    for x in stringList:
        counter = 0
        for y in stringList:
            if x == y:
                counter += 1
        charCounter.append(counter)
    
    # iterate through the charCounter, if there are more than one odd number then return false
    oddCharCount = 0
    for x in charCounter:
        if (x % 2 != 0):
            oddCharCount += 1
    
    if oddCharCount > 1:
        return False
    else:
        return True

""" Check to see if two given strings are one insert, removal, or replacement away"""
def oneAway(str1, str2):
    
    strList1 = []
    for x in str1:
        strList1.append(x)
    
    strList2 = []
    for x in str2:
        strList2.append(x)

    if str1 == str2:
        print("They are the same string")

    # if they are one insert, they have to off by one on length 
    elif (len(strList1) + 1) == len(strList2):

        index1 = 0
        index2 = 0

        while(index1 < len(strList1) and index2 < len(strList2)):
            if (strList1[index1] != strList2[index2]):
                if (index1 != index2):
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1

            return True


    # if they are one removal they have to be off by one on length
    elif (len(strList1) - 1) == len(strList2):

        index1 = 0
        index2 = 0

        while(index1 < len(strList2) and index2 < len(strList1)):
            if (strList1[index1] != strList2[index2]):
                if (index1 != index2):
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1

            return True

    # if they are one replacement they have to be same length 
    elif (len(strList1) == len(strList2)):

        differenceCounter = 0

        for x in range(len(strList1)):

            if (strList1[x] != strList2[x]):
                differenceCounter += 1

        if differenceCounter > 1:
            return False
        else:
            return True
    
    else:
        return False
        
        


        

    




            



main()