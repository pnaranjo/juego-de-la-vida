

def matriz_minima(rows, columns):
    if (int(rows) >= 3 and int(columns) >= 3):
        return True
    else:
        print ('el minimo es 3 x 3')
        return False

def cells_max_matriz(cells, rows, columns):
    if cells > rows * columns:
        print('\nLas celulas vivas no pueden exceder la matriz\n')
        input('**** toque una tecla para continuar ****')
        return True
    else:
        return False
