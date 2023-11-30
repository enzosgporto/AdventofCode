#part one

with open('2022/Day 01/day1input.txt') as f: #opens text file with the variable f
    contents = f.read() #assigns content 

    a = 0
    sumOfElements = 0

    for i in contents.split("\n\n"): #split the code every two lines (per elf)
        a = 0
        currentList = i.split("\n") #splits the code per line
        for j in currentList:
            j = int(j)
            a +=j
        if a > sumOfElements: 
            sumOfElements = a

    print("The elf with the most calories has {} calories".format(sumOfElements))

#part two

with open('2022/Day 01/day1input.txt') as f: #opens text file with the variable f
    contents = f.read() #assigns content 

    elf1 = 0
    elf2 = 0
    elf3 = 0

    for i in contents.split("\n\n"): #split the code every two lines (per elf)
        currentSum = 0
        currentList = i.split("\n") #splits the code per line
        for j in currentList:
            j = int(j)
            currentSum +=j
        if currentSum > elf1: 
            elf3 = elf2
            elf2 = elf1
            elf1 = currentSum
        elif currentSum > elf2:
            elf3 = elf2
            elf2 = currentSum
        elif currentSum > elf2:
            elf3 = currentSum

    print("The elf with the most calories has {} calories \n The elf with the second most calories has {} calories \n The elf with the third most calories has {} calories".format(elf1, elf2, elf3))