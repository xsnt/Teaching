def cleanTable():
    matriz = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return matriz


def printTable(table):
    for i in table:
        print (i)


def checkDiag(table,char):
    condVit = 0
    for i in range(3):
        if table[i][i] == char:
            condVit += 1
    if condVit == 3:
        return True
    else:  
        return False


def checkCounterDiag(table, char):
    condVit = 0
    linha = 0
    for i in range(2, 0, -1):
        if table[linha][i] == char:
            condVit += 1
        linha += 1
    
    if condVit == 3:
        return True
    else:  
        return False


def vertCheck(table, char):
    condVit = 0
    for y in range(3):
        for x in range(3):
            #if y == x:
            if table[x][y] == char:
                condVit += 1
        if condVit == 3:
            return True
        else:
            condVit = 0


def horCheck(table, char):
    condVit = 0
    for x in range(3):
        for y in range(3):
            #if y == x:
            if table[x][y] == char:
                condVit += 1
        if condVit == 3:
            return True
        else:
            condVit = 0


def tableCheck(table, char):
    check = vertCheck(table, char)
    if check == True:
      return check
    check = horCheck(table, char)
    if check == True:
      return check
    check = checkCounterDiag(table, char)
    if check == True:
      return check
    check = checkDiag(table, char)
    return check


while True:
    print ("Game starting!")
    m1 = cleanTable()
    turns = 0
    while True:
        turns += 1
        print ("Turn ", turns)
        print ("X Turn!")
        x = int(input("Choose a line: "))
        y = int(input("Choose a column: "))
        m1[x][y] = "X"
        printTable(m1)
        check = tableCheck(m1, "X")
        if check == True:
            print ("X Wins!")
            break
        print ("Y Turn!")
        x = int(input("Choose a line: "))
        y = int(input("Choose a column: "))
        m1[x][y] = "Y"
        printTable(m1)
        check = tableCheck(m1, "Y")
        if check == True:
            print ("Y Wins!")
            break
    print ("Game ended in {turns} turns.")
    replay = input ("Do you wish to play again? Y or N").upper
    while True:
        if replay != "Y" or replay != "Y": 
            print ("Answer not expected, please try again.")
            replay = input ("Do you wish to play again? Y or N").upper
        elif replay == "Y" or replay == "Y":
            break 
    if replay == "N":
        print ("Cya!")
        break
    elif replay == "Y":
        print ("Ok! Restarting...")