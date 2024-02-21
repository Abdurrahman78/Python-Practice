def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return all((isTwoLetters(s),maxMin(s),middleNumbers(s),noPunc(s)))

#All vanity plates must start with at least two letters.
def isTwoLetters(plate):
    twoLetter=plate[0:2]
    if twoLetter.isalpha():
        return True
    else:
        return False


#vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def maxMin(plate):
    if len(plate)<=6 and len(plate)>=2:
        return True
    else:
        return False

#Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
#AAA22A would not be acceptable. The first number used cannot be a ‘0’
#AAA2A2222A

def middleNumbers(plate):
    #lets first check the first number is not zero
    numberString=""
    for char in plate:
        if char.isnumeric():
            numberString+=char

#now lets check middle numbers
    for char in range(len(plate)-1):
        if len(plate)>1:
            letterCheck=plate[char+1]
        if plate[char].isnumeric() and letterCheck.isalpha():
            return False
        elif len(numberString)>0 and numberString[0]=="0":
            return False
        else:
            continue

    return True

#No periods, spaces, or punctuation marks are allowed
def noPunc(plate):
    for char in range(len(plate)):
        if plate[char].isalpha() or plate[char].isnumeric():
            continue
        else:
            return False

    return True

if __name__ == "__main__":
    main()
