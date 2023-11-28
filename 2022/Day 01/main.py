with open('input.txt') as f:
    contents = f.read()

    fileList = contents.split("\n\n")
    a = 0
    sumOfElements = 0

    for i in fileList: 
        a = 0
        currentList = i.split("\n")
        for j in currentList:
            j = int(j)
            a +=j
        if a > sumOfElements:
            sumOfElements = a

    print(sumOfElements)