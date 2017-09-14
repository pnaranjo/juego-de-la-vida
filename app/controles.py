class controles(object):


    def __init__(self):
        pass
        
    def matriz_minima(self,rows, columns):
        if (int(rows) >= 3 and int(columns) >= 3):
            return True
        else:
            print ('el minimo es 3 x 3')
            return False
    
    def cells_max_matriz(self,cells, rows, columns):
        if cells > rows * columns:
            print('\nLas celulas vivas no pueden exceder la matriz\n')
            input('**** toque una tecla para continuar ****')
            return True
        else:
            return False
    
    def control_ubicacion_disponible(self,row, column, patron):
        try:
            if patron[row][column] == 1:
                print('\n***** Ubicacion invalida *****\n')
                return False
            else:
                return True
        except IndexError:
            print('\n***** Ubicacion invalida *****\n')
            return False
