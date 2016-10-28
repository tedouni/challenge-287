#Main challenge: Write a function that, given a 4-digit number, returns the largest digit in that number. Numbers between 0 and 999 are counted as 4-digit numbers with leading 0's.

def largest_digit(numA):
    tempMax = 0
    iterate = str(numA)

    for digit in iterate:
        if int(digit) > tempMax:
            tempMax = int(digit)
    return tempMax

#Bonus 1
def desc_digits(numA):
    tempList = []
    digitLen = len(str(numA))
    iterate = str(numA)
    returnString = ''
    if digitLen == 4:
        for digit in iterate:
            tempList.append(digit)
        tempList.sort()
        for item in reversed(tempList):
            returnString += (str(item))
    else:
        numOfInserts = 4 - digitLen
        for i in range(0,numOfInserts):
            tempList.append(0)
        for digit in iterate:
            tempList.append(digit)
        tempList.sort()
        for item in reversed(tempList):
            returnString += (str(item))

    return int(returnString)

#Bonus 2

def kaprekar(numA):
    returnResult = 0
    tempNum = numA

    if numA != 6174:
        while(tempNum > 0):
            digitLen = len(str(tempNum))
            ascendingList =''
            descendingList = ''
            iterate = str(tempNum)
            tempList = []
            if digitLen < 4:
                numOfInserts = 4 - digitLen
                for i in range(0,numOfInserts):
                    tempList.append(0)
                for digit in iterate:
                    tempList.append(digit)
            else:
                for digit in iterate:
                    tempList.append(digit)
            tempList.sort()
            for digit in tempList:
                ascendingList += str(digit)
            for digit in reversed(tempList):
                descendingList += str(digit)
            tempNum = int(descendingList) - int(ascendingList)
            # print tempNum
            returnResult += 1
            if int(tempNum) == 6174:
                break
    return returnResult

def main():
    print 'Main Challenge:'
    print 'largest_digit(1234) -> ' +  str(largest_digit(1234))
    print 'largest_digit(3253) -> ' +  str(largest_digit(3253))
    print 'largest_digit(9800) -> ' +  str(largest_digit(9800))
    print 'largest_digit(3333) -> ' +  str(largest_digit(3333))
    print 'largest_digit(120) -> ' +  str(largest_digit(120))
    print '\nBonus 1:'
    print 'desc_digits(1234) -> ' + str(desc_digits(1234))
    print 'desc_digits(3253) -> ' + str(desc_digits(3253))
    print 'desc_digits(9800) -> ' + str(desc_digits(9800))
    print 'desc_digits(3333) -> ' + str(desc_digits(3333))
    print 'desc_digits(120) -> ' + str(desc_digits(120))
    print '\nBonus 2:'
    print 'kaprekar(6589) -> '+ str(kaprekar(6589))
    print 'kaprekar(5455) -> '+ str(kaprekar(5455))
    print 'kaprekar(6174) -> '+ str(kaprekar(6174))
    
if __name__ == '__main__':
    main()
