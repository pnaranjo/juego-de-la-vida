import random, os, time, pdb, copy, math

from controles import controles
from combination import combinations



class juego_de_la_vida(object):

    def __init__(self, actualTable=[]):
        self.control = controles()
        self.actualTable = actualTable
        self.futureTable = []
        self.modo_f = False
        self.finished = False
        self.modo = None
        self.started = False
        self.modo_ve = False
        self.iter_list_x = []
        self.iter_list_y = []


    def prepare_game(self):
        while True:
            rows = input("Introduce la cantidad de filas que deseas:")
            columns = input("Introduce la cantidad de columnas que deseas:")

            if not self.control.verify_input_int(rows,columns):
                not_int = True
                while not_int:
                    rows = input("Introduce la cantidad de filas que deseas:")
                    columns = input("Introduce la cantidad de columnas que deseas:")
                    not_int = not self.control.verify_input_int(rows,columns)

            if self.control.matriz_minima(rows,columns):
                break
        return int(rows), int(columns)

    def game(self, rows, columns, patron=None):



        if not self.actualTable: self.loadActualTable(rows,columns, patron)
        self.loadFutureTable(rows,columns)
        self.checkLife(rows, columns)

    def checkLife(self, rows, cols):
        table2 = []
        while True:

            try:

                self.magic(rows, cols)
                self.actualTable, self.futureTable = self.futureTable, self.actualTable

                table1 = table2[:]
                table2 = copy.deepcopy(self.futureTable)

                os.system('clear')
                self.paintTable(self.futureTable, rows , cols)

                if not self.modo_f and not self.modo_ve:
                    self.menu_secundario(self.futureTable)
                elif self.es_estatico():
                    input('el juego termino por encontrar un patron estatico')
                    raise KeyboardInterrupt
                elif self.oscila(table1):
                      input('el juego termino por encontrar un patron oscilante nivel 2')
                      raise KeyboardInterrupt
                time.sleep(1)
                self.resetFutureTable(rows , cols)


            except (EOFError, KeyboardInterrupt):
                self.started = True
                break

    def magic(self, rows, cols):
        container = [
                     [0,0,0],
                     [0,0,0],
                     [0,0,0]
                    ]

        self.check_corners(rows,cols)
        self.check_extremos(rows,cols,'superior') #lateral superior
        self.check_extremos(rows,cols,'inferior')
        self.check_lateral(rows,cols,'derecho')
        self.check_lateral(rows,cols,'izquierdo')

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


                if (cellCounter < 2 or cellCounter > 3) and container[1][1] == 1:
                    self.futureTable[row + 1][col + 1] = 0

                elif cellCounter > 3 and container[1][1] == 1:
                    self.futureTable[row + 1][col + 1] = 0

                elif cellCounter == 3 and container[1][1] == 0:
                    self.futureTable[row + 1][col + 1] = 1

                elif (cellCounter == 3 or cellCounter == 2) and container[1][1] == 1:
                    self.futureTable[row + 1][col + 1] = 1

    def check_corners(self, rows, cols):
            vivos = 0
            #esquina [0,0]
            if self.actualTable[0][1] == 1:
                vivos += 1
            if self.actualTable[1][0] == 1:
                vivos += 1
            if self.actualTable[1][1] == 1:
                vivos += 1
            if self.actualTable[0][0] == 0 and vivos == 3:
                self.futureTable[0][0] = 1
            if self.actualTable[0][0] == 1 and vivos >= 2:
                self.futureTable[0][0] = 1

            vivos = 0
            #esquina [0,fin]
            if self.actualTable[0][-2] == 1:
                vivos += 1
            if self.actualTable[1][-2] == 1:
                vivos += 1
            if self.actualTable[1][-1] == 1:
                vivos += 1
            if self.actualTable[0][-1] == 0 and vivos == 3:
                self.futureTable[0][-1] = 1
            if self.actualTable[0][-1] == 1 and vivos >= 2:
                self.futureTable[0][-1] = 1

            vivos = 0
            #esquina [fin,0]
            if self.actualTable[-1][1] == 1:
                vivos += 1
            if self.actualTable[-2][0] == 1:
                vivos += 1
            if self.actualTable[-2][1] == 1:
                vivos += 1
            if self.actualTable[-1][0] == 0 and vivos == 3:
                self.futureTable[-1][0] = 1
            if self.actualTable[-1][0] == 1 and vivos >= 2:
                self.futureTable[-1][0] = 1

            vivos = 0
            #esquina [fin,fin]
            if self.actualTable[-1][-2] == 1:
                vivos += 1
            if self.actualTable[-2][-1] == 1:
                vivos += 1
            if self.actualTable[-2][-2] == 1:
                vivos += 1
            if self.actualTable[-1][-1] == 0 and vivos == 3:
                self.futureTable[-1][-1] = 1
            if self.actualTable[-1][-1] == 1 and vivos >= 2:
                self.futureTable[-1][-1] = 1

    def check_extremos(self, rows, cols, lado):
        container = [[0,0,0],
                     [0,0,0]]

        # lateral superior
        if lado == 'superior':
            rowC = 0
            colC = 1
            row = 0
            rowcell1 = row
            rowcell2 = row
            rowcell3 = row
            rowcell4 = row + 1
            rowcell5 = row + 1
            rowcell6 = row + 1

        elif lado == 'inferior':
            rowC = 1
            colC = 1
            row = -1
            rowcell1 = row - 1
            rowcell2 = row - 1
            rowcell3 = row - 1
            rowcell4 = row
            rowcell5 = row
            rowcell6 = row

        for col in range(cols -2):
            cell1 = self.actualTable[rowcell1][col]
            cell2 = self.actualTable[rowcell2][col + 1]
            cell3 = self.actualTable[rowcell3][col + 2]
            cell4 = self.actualTable[rowcell4][col]
            cell5 = self.actualTable[rowcell5][col + 1]
            cell6 = self.actualTable[rowcell6][col + 2]


            container[0][0] = cell1
            container[0][1] = cell2
            container[0][2] = cell3
            container[1][0] = cell4
            container[1][1] = cell5
            container[1][2] = cell6

            cellCounter = 0
            for rowContainer in range(2):
                for colContainer in range(3):

                    if not (rowContainer == rowC and colContainer == colC):
                        if container[rowContainer][colContainer] == 1:
                            cellCounter = cellCounter + 1


            if (cellCounter < 2 or cellCounter > 3) and container[rowC][colC] == 1:
                self.futureTable[row][col + colC] = 0

            elif cellCounter > 3 and container[rowC][colC] == 1:
                self.futureTable[row][col + colC] = 0

            elif cellCounter == 3 and container[rowC][colC] == 0:
                self.futureTable[row][col + colC] = 1

            elif (cellCounter == 3 or cellCounter == 2) and container[rowC][colC] == 1:
                self.futureTable[row][col + colC] = 1



    def check_lateral(self, rows, cols, lado):
        container = [[0,0],
                     [0,0],
                     [0,0]]

        if lado == 'derecho':
            rowC = 1
            colC = 1
            col = -1
            colcell1 = col - 1
            colcell2 = col
            colcell3 = col - 1
            colcell4 = col
            colcell5 = col - 1
            colcell6 = col

        elif lado == 'izquierdo':
            rowC = 1
            colC = 0
            col = 0
            colcell1 = col
            colcell2 = col + 1
            colcell3 = col
            colcell4 = col + 1
            colcell5 = col
            colcell6 = col + 1

        for row in range(rows -2):
            cell1 = self.actualTable[row][colcell1]
            cell2 = self.actualTable[row][colcell2]
            cell3 = self.actualTable[row + 1][colcell3]
            cell4 = self.actualTable[row + 1][colcell4]
            cell5 = self.actualTable[row + 2][colcell5]
            cell6 = self.actualTable[row + 2][colcell6]


            container[0][0] = cell1
            container[0][1] = cell2
            container[1][0] = cell3
            container[1][1] = cell4
            container[2][0] = cell5
            container[2][1] = cell6

            cellCounter = 0
            for rowContainer in range(3):
                for colContainer in range(2):

                    if not (rowContainer == rowC and colContainer == colC):
                        if container[rowContainer][colContainer] == 1:
                            cellCounter = cellCounter + 1


            if (cellCounter < 2 or cellCounter > 3) and container[rowC][colC] == 1:
                self.futureTable[row + rowC][col] = 0

            elif cellCounter > 3 and container[rowC][colC] == 1:
                self.futureTable[row + rowC][col] = 0

            elif cellCounter == 3 and container[rowC][colC] == 0:
                self.futureTable[row + rowC][col] = 1

            elif (cellCounter == 3 or cellCounter == 2) and container[rowC][colC] == 1:
                self.futureTable[row + rowC][col] = 1


    def es_estatico(self):
        if self.actualTable == self.futureTable:
            return True
        else:
            return False

    def oscila(self, tabla):
        if tabla == self.actualTable:
            return True
        else:
            return False

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
            row = input('ingrese fila a modificar: ')
            col = input('ingrese columna a modificar: ')
            if not self.control.control_ubicacion_disponible(row, col, table):
                invalid_input = True
                while invalid_input:
                    row = input('ingrese fila a modificar: ')
                    col = input('ingrese columna a modificar: ')
                    invalid_input = not self.control.control_ubicacion_disponible(row, col, table)
                self.modify_cel(table, int(row), int(col))


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
        for row in range(rows):
            for col in range(columns):

                if actualTable[row][col] == 1:
                    print (" * " , end='')

                else:
                    print (" - "  , end='')

                if col == columns -1: print('')
        self.printLine()





    def loadActualTable(self, rows , columns, patronArray=None):

        for row in range(rows):
            for col in range(columns):

                newArray = []
                for zeroValue in range(columns):
                    newArray.append(0)
            self.actualTable.append(newArray)

        if patronArray:
            for i in patronArray:
                row=i[0]
                col=i[1]
                self.actualTable[row][col] = 1

        else:
            for row in range(rows):
                for col in range(columns):
                    value = random.randint(0,1)

                    if value == 1:
                        self.actualTable[row][col] = 1


    def loadFutureTable(self, rows , columns):
        for row in range(rows):

            newArray = []
            for zeroValue in range(columns):
                newArray.append(0)

            self.futureTable.append(newArray)

        for row in range(rows):
            for col in range(columns):
                self.futureTable[row][col] = 0





    def resetFutureTable(self, rows , cols):
        for row in range(rows):
            for col in range(cols):
                self.futureTable[row][col] = 0

    def resetActualTable(self, rows , cols):
        for row in range(rows):
            for col in range(cols):
                self.actualTable[row][col] = 0

    def vidas_estaticas(self, rows, cols, cells, cantidad=0, contador_estatico=0):
        self.modo_ve = True
        while True:
            try:
                if not self.iter_list_x: self.iter_list_x = iter(combinations(range(rows*cols),cells))
                for x in self.iter_list_x:
                    cantidad += 1
                    patron = []

                    if not self.iter_list_y: self.iter_list_y = range(cells)
                    for y in self.iter_list_y:
                        fila = math.floor((x[y] / rows))
                        columna = x[y] % rows
                        patron.append((fila,columna))


                    self.loadActualTable(rows,cols, patron)
                    self.loadFutureTable(rows,cols)
                    self.magic(rows, cols)
                    if self.es_estatico():
                       self.paintTable(self.actualTable, rows, cols)
                       contador_estatico = contador_estatico + 1
                    self.actualTable = []
                    self.futureTable = []

                print('Vidas estaticas: ' + str(contador_estatico))
                print('Combinaciones posibles: ' + str(cantidad))
                input()
                self.modo_ve = False
                self.modo = None
                self.started = False
                self.iter_list_x = []
                self.iter_list_y = []
                break
            except (KeyboardInterrupt):
                if not self.actualTable or not self.futureTable:
                    self.loadActualTable(rows,cols, patron)
                    self.loadFutureTable(rows,cols)
                self.cantidad = cantidad
                self.contador_estatico = contador_estatico
                self.started = True
                break
        self.modo_ve = False
