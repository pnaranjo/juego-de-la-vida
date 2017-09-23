import random
import os
import time
from controles import controles

class juego_de_la_vida(object):


    def __init__(self, actualTable=[]):
        self.control = controles()
        self.actualTable = actualTable
        self.futureTable = []
        self.modo_f = False
        self.finished = False
        self.modo = None
        self.started = False


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

        if not self.actualTable: self.loadActualTable(self.actualTable,rows,columns, patron)
        self.loadFutureTable(self.futureTable,rows,columns)
        self.checkLife(self.actualTable, self.futureTable, container, rows, columns)

    def checkLife(self,actualTable ,futureTable , container , rows, cols):

        while True:
            try:
                for row in range(rows -2):
                    for col in range(cols -2):

                        cell1 = self.actualTable[row][col]
                        cell2 = self.actualTable[row][col + 1]
                        cell3 = self.actualTable[row][col + 2]

                        cell4 = self.actualTable[row + 1][col]
                        cell5 = self.actualTable[row + 1][col + 1]
                        cell6 = self.actualTable[row + 1][col + 2]

                        cell7 = self.actualTable[row + 2][col]
                        cell8 = self.actualTable[row + 2][col + 1]
                        cell9 = self.actualTable[row + 2][col + 2]


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
                            self.futureTable[row + 1][col + 1] = 0

                        elif cellCounter > 3 and container[1][1] == 1:
                            self.futureTable[row + 1][col + 1] = 0

                        elif cellCounter == 3 and container[1][1] == 0:
                            self.futureTable[row + 1][col + 1] = 1

                        elif cellCounter == 3 and container[1][1] == 1:
                            self.futureTable[row + 1][col + 1] = 1

                        elif cellCounter == 2:
                            self.futureTable[row +1][col + 1] = self.actualTable[row +1][col +1]


                auxiliarTable = self.actualTable
                self.actualTable = self.futureTable
                self.futureTable = auxiliarTable

                os.system('clear')
                self.paintTable(self.futureTable, rows , cols)
                if not self.modo_f:
                    self.menu_secundario(self.futureTable)
                else:
                    time.sleep(1)
                self.resetTable(self.futureTable, rows , cols)

            except (EOFError, KeyboardInterrupt):
                self.started = True
                break

    def menu_secundario(self, table):
        print ('*' * 40 )
        print ('- Presiona "n" para pasar al siguiente paso')
        print ('- Presiona "m" para modificar una celda')
        print ('- Presiona "f" para ejecutar hasta encontrar un patron estatico o oscilador')
        print ('- Preciona "Ctrl + C" para volver al menu principal')
        print ('*' * 40 )

        a = input('Elige una opcion: ')

        if a == "n":
            pass

        elif a == "m":
            #TODO: poner control
            col = int(input('ingrese columna a modificar: '))
            row = int(input('ingrese fila a modificar: '))
            self.modify_cel(table, row, col)


        elif a == "f":
            self.modo_f = True


        else:
            print("opcion no valida")
            self.menu_secundario(table)




    def modify_cel(self, tabla, row, col):
        if tabla[row][col] == 1:
            tabla[row][col] = 0
        else:
            tabla[row][col] = 1


    def printLine(self):
        print('----' * 10)

    def paintTable(self,actualTable , rows , columns):
        print(actualTable)
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
            for i in patronArray:
                row=i[0]
                col=i[1]
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
