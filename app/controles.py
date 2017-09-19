#!/usr/bin/python3
# Version 1.0

def matriz_minima(rows, columns):
    if (int(rows) >= 3 and int(columns) >= 3):
        ''' Parametros de entrada rows, columns
        Controla que el minimo sea de 3 x 3
        si cumple retorna True
        '''
        return True
    else:
        print ('el minimo es 3 x 3')
        return False

def cells_max_matriz(cells, rows, columns):
    ''' Parametros de entrada cells, rows, columns
        Controla que la cantidad cells (celulas vivas)
        no exedan a la matriz
        Si supera retorna True
    '''
    if cells > rows * columns:
        print('\nLas celulas vivas no pueden exceder la matriz\n')
        input('**** toque una tecla para continuar ****')
        return True
    else:
        return False

def control_ubicacion_disponible(row, column, patron):
    ''' Parametros de entrada row, colum, patron
        Controla que la fila y columna de un
        patron (matriz) no este viva ni se exeda
        de los limites
        Retorna True si esta dentro de la matriz
        y el casillero esta muerto
    '''
    try:
        if patron[row][column] == 1:
            print('\n***** Fila repetida *****\n')
            return False
        else:
            return True
    except IndexError:
        print('\n***** Ubicacion invalida, fuera de limite *****\n')
        return False
