import random
import os
import time

def prepare_game():
    rows = input("Introduce la cantidad de filas que deseas:")
    columns = input("Introduce la cantidad de columnas que deseas:")
    return int(rows), int(columns)

def game():
    rows, columns = prepare_game()

    container = [
                 [0,0,0],
                 [0,0,0],
                 [0,0,0]
                ]

    actualTable = []
    futureTable = []

    loadActualTable(actualTable,rows,columns)
    loadFutureTable(futureTable,rows,columns)

    checkLife(actualTable, futureTable, container, rows, columns)


def checkLife(actualTable ,futureTable , container , rows, cols):

    while True:

        for row in range(rows -2):
            for col in range(cols -2):

                cell1 = actualTable[row][col]
                cell2 = actualTable[row][col + 1]
                cell3 = actualTable[row][col + 2]

                cell4 = actualTable[row + 1][col]
                cell5 = actualTable[row + 1][col + 1]
                cell6 = actualTable[row + 1][col + 2]

                cell7 = actualTable[row + 2][col]
                cell8 = actualTable[row + 2][col + 1]
                cell9 = actualTable[row + 2][col + 2]


                container[0][0] = cell1
                container[0][1] = cell2
                container[0][2] = cell3

                container[1][0] = cell4
                container[1][1] = cell5
                container[1][2] = cell6

                container[2][0] = cell7
                container[2][1] = cell8
                container[2][2] = cell9

                cellCounter = 0

                for rowContainer in range(3):
                    for colContainer in range(3):

                        if not (rowContainer == 1 and colContainer == 1):
                            if container[rowContainer][colContainer] == 1:
                                cellCounter = cellCounter + 1


                if cellCounter < 2 and container[1][1] == 1:
                    futureTable[row + 1][col + 1] = 0

                elif cellCounter > 3 and container[1][1] == 1:
                    futureTable[row + 1][col + 1] = 0

                elif cellCounter == 3 and container[1][1] == 0:
                    futureTable[row + 1][col + 1] = 1

                elif cellCounter == 3 and container[1][1] == 1:
                    futureTable[row + 1][col + 1] = 1

                elif cellCounter == 2:
                    futureTable[row +1][col + 1] = actualTable[row +1][col +1]


        auxiliarTable = actualTable
        actualTable = futureTable
        futureTable = auxiliarTable

        os.system('clear')
        paintTable(futureTable, rows , cols)
        resetTable(futureTable, rows , cols)
        time.sleep(.4)



def printLine():
    print("----------------------------------------------------------------------------")

def paintTable(actualTable , rows , columns):

    for row in range(rows):
        for col in range(columns):

            if actualTable[row][col] == 1:
                print ("| O " , end='')

            else:
                print ("|   "  , end='')

            if col == columns -1: print('')

        printLine()




def loadActualTable(actualTable , rows , columns):

    for row in range(rows):
        for col in range(columns):

            newArray = []
            for zeroValue in range(columns):
                newArray.append(0)

            actualTable.append(newArray)


    for row in range(rows):
        for col in range(columns):
            value = random.randint(0,1)

            if value == 1:
                actualTable[row][col] = 1


def loadFutureTable(futureTable , rows , columns):

    for row in range(rows):
        for col in range(columns):

            newArray = []
            for zeroValue in range(columns):
                newArray.append(0)

            futureTable.append(newArray)

    for row in range(rows):
        for col in range(columns):
            futureTable[row][col] = 0



def resetTable(table , rows , cols):
    for row in range(rows):
        for col in range(cols):
            table[row][col] = 0


# Call game
game()
