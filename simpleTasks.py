#! /usr/local/bin/python3.4

from collections import Counter

def find(pattern):
    inptr = open("sequence.txt", 'r')
    if inptr.mode == 'r':                                       #Checks to make sure the file is open
        sequence = inptr.read()
    else:
        print("Could not open file")

    matches = []
    for i in range(len(sequence) - (len(pattern) - 1)):
        number = sequence[i: len(pattern) + i]
        for j in range(len(pattern)):
            if pattern[j] != 'X' and pattern[j] == number[j]:
                matches.append([number, i])
    matches = Counter(map(tuple, matches))                      #find all the number of occurences in a list of lists
    matches = matches.most_common()                             #count occurence and returns it
    matches.sort(key=lambda x:x[1])

    digits = 0
    for item in pattern:
        if item != 'X':
            digits += 1

    for i in range(len(matches)):
        if matches[i][1] == digits:
            matches[i] = matches[i][0][0]
    matches = [x for x in matches if isinstance(x, str)]
    return matches

def getStreakProduct(sequence, maxSize, product):
    equalProduct = []

    for i in range(2, maxSize + 1):
        for j in range(len(sequence) - (i - 1)):
            subSeq = sequence[j: i + j]
            prod = 1
            for num in subSeq:
                prod *= int(num)
            if prod == product:
                equalProduct.append([subSeq, j])
    equalProduct.sort(key=lambda x:x[1])

    for i in range(len(equalProduct)):
        equalProduct[i] = equalProduct[i][0]

    return equalProduct

def writePyramids(filePath, baseSize, count, char):
    outptr =  open(filePath, 'w')
    if outptr.mode == 'w':
        for i in range(1,baseSize + 1,2):
            outptr.write('{:^{}} '.format(char * i, baseSize) * count)
            outptr.write("\n")
    outptr.close()

def getStreaks(sequence, letters):
    matches = []
    for letter in letters:
        seq = ''
        for i in range(len(sequence)):
            if letter == sequence[i]:
                seq += letter
            else:
                if seq:
                    matches.append([seq, i])
                    seq = ''
        if seq:                                     #If the string is not empty append
            matches.append([seq, i])
    matches.sort(key=lambda x: x[1])                #Sort list of lists by the apperance (2nd element)
    for i in range(len(matches)):
        matches[i] = matches[i][0]
    return matches

def findNames(nameList, part, name):
    names = []
    for person in nameList:
        firstName, lastName = person.split()
        if part == 'F' and name.capitalize() == firstName:
            names.append(person)
        elif part == 'L' and name.capitalize() == lastName:
            names.append(person)
        elif part == 'FL' and (name.capitalize() == firstName or name.capitalize() == lastName):
            names.append(person)
    return names

def convertToBoolean(num, size):
    if not all(isinstance(i, int) for i in [num, size]):    #Verify that the input parameters are integers, return an empty list if they are not
        return []
    binary = bin(num)[2:]
    boolList = []
    for number in binary:
        boolList.append(bool(int(number)))
    while size > len(binary):
        boolList.insert(0, bool(0))                         #Expands the list to satisfy the needs of the input number if the requested size is not sufficient
        size -= 1
    return boolList

def convertToInteger(boolList):
    if not isinstance(boolList, list):       #Verify that input is a list, if not a list returns None
         return None
    if not boolList:                         #Verify that the list is not empty, if empty return none
        return None
    integer = ''
    for item in boolList:
        if not isinstance(item, bool):       #Verify that each element is a boolean, return none otherwise
            return None
        integer += str(int(item))
    return int(integer, 2)

if __name__=="__main__":
    #bList = [True, False, False, False, False, True, True, True]
    #bList = [False, False, True, False, False, True]
    #print(convertToInteger(bList))

    #print(convertToBoolean(135, 12))
    #print(convertToBoolean("Enoch", 3))
    #print(convertToBoolean(135, "3"))

    #nameList = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    #print(findNames(nameList, 'L', "johnson"))
    #print(findNames(nameList, 'F', "JOHNSON"))
    #print(findNames(nameList, 'A', "Johnson"))

    #sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    #print(getStreaks(sequence, "SAQT"))
    #print(getStreaks(sequence, "PAZ"))
    #print(getStreaks(sequence, "KID"))

    #print(getStreakProduct("14822", 3, 32))
    #print(getStreakProduct("54789654321687984", 5, 0))

    #print(find("X38X"))

    writePyramids("filePath.txt", 15, 5, '*')

