#Part 1

sumOfDigits = 0

with open('enzoInput.txt') as f:
    contents = f.read()
    lineArray = contents.split("\n") #splits the code per line


    i = 0 #sets i to zero
    digitsArray = [] #creates array for the digits

    for line in lineArray: #loops through each line of the code
        digitsArray.append([]) #creates a new array inside of the array
        for character in line: #loops through each character in the string
            if character.isdigit(): #checks whether the character is a digit (0-9)
                digitsArray[i].append(character) #appends the character for the current new array
        i += 1 #increases i by 1 when line is over (so next line enters on a new array)
        
    
    a = 0

for a in range(len(digitsArray)):
    firstDigit = digitsArray[a][0] #sets first digit to be index 0 of the current list
    print("First digit is {}".format(firstDigit))

    secondDigit = digitsArray[a][len(digitsArray[a])-1] #sets last digit to be index list length - 1 of the current list
    print("Second digit is {}".format(secondDigit))

    digit = firstDigit + secondDigit #concanates both strings to create the digit
    print("The digit is {}".format(digit))

    sumOfDigits += int(digit) #transforms string into number and adds it to the sum    
    print("Therefore the sum is {}".format(sumOfDigits))

    a += 1


print(sumOfDigits) #prints sum of digits