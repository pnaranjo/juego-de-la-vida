import random
import os
from controles import controles

class juego_de_la_vida(object):


    def __init__(self):
        self.control = controles()

    def prepare_game(self):
        while True:
            rows = input("Introduce la cantidad de filas que deseas:")
            columns = input("Introduce la cantidad de columnas que deseas:")
            if self.control.matriz_minima(rows,columns):
                break
        return int(rows), int(columns)

    def game(self, rows, columns, patron=None):

        container = [
                     [0,0,0],
                     [0,0,0],
                     [0,0,0]
                    ]

        actualTable = []
        futureTable = []

        self.loadActualTable(actualTable,rows,columns, patron)
        self.loadFutureTable(futureTable,rows,columns)

        self.checkLife(actualTable, futureTable, container, rows, columns)


    def checkLife(self,actualTable ,futureTable , container , rows, cols):

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
            self.paintTable(futureTable, rows , cols)
            self.resetTable(futureTable, rows , cols)
            if not self.menu_secundario(actualTable):
                break


    def menu_secundario(self, actualTable):
        print ('*' * 40 )
        print ('- Presiona "n" para pasar al siguiente paso')
        print ('- Presiona "m" para modificar una celda')
        print ('- Presiona "f" para ejecutar hasta encontrar un patron estatico o oscilador')
        print ('- Preciona "Ctrl + C" para volver al menu principal')
        print ('*' * 40 )
        
        try:
            a = input('Elige una opcion: ')

            if a == "n":
                pass

            elif a == "m":
                #TODO: poner control
                col = int(input('ingrese columna a modificar: '))
                row = int(input('ingrese fila a modificar: '))
                self.modify_cel(actualTable, row, col)


            elif a == "f":
                #TODO: patron estatico o oscilador
                pass

            else:
                print("opcion no valida")
                self.menu_secundario()

            return True
        except (EOFError, KeyboardInterrupt):
            return False



    def modify_cel(self, tabla, row, col):
        if tabla[row][col] == 1:
            tabla[row][col] = 0
        else:
            tabla[row][col] = 1


    def printLine(self):
        print('----' * 10)

    def paintTable(self,actualTable , rows , columns):

        for row in range(rows):
            for col in range(columns):

                if actualTable[row][col] == 1:
                    print ("|* " , end='')

                else:
                    print ("|- "  , end='')

                if col == columns -1: print('')
        self.printLine()





    def loadActualTable(self,actualTable , rows , columns, patronArray=None):

        for row in range(rows):
            for col in range(columns):

                newArray = []
                for zeroValue in range(columns):
                    newArray.append(0)

                actualTable.append(newArray)

        if patronArray:
            print(patronArray)
            for i in patronArray:
                row=i[0]
                col=i[1]
                print(i[0])
                actualTable[row][col] = 1

        else:
            for row in range(rows):
                for col in range(columns):
                    value = random.randint(0,1)

                    if value == 1:
                        actualTable[row][col] = 1


    def loadFutureTable(self,futureTable , rows , columns):

        for row in range(rows):
            for col in range(columns):

                newArray = []
                for zeroValue in range(columns):
                    newArray.append(0)

                futureTable.append(newArray)

        for row in range(rows):
            for col in range(columns):
                futureTable[row][col] = 0



    def resetTable(self,table , rows , cols):
        for row in range(rows):
            for col in range(cols):
                table[row][col] = 0


    # Call game
    #game()
