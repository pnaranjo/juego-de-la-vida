#!/usr/bin/python
# Version 1.0

from juego_de_la_vida import juego_de_la_vida
from controles import controles
import os, pickle, time, json
from random import shuffle
import pdb

class menu(object):

    def __init__(self):
        self.control = controles()
        self.juego = juego_de_la_vida()
        self.mostrar_menu()


    def mostrar_menu(self):
        menu = {}
        menu['01'] = 'Patron random'
        menu['02'] = 'Patron específico'
        menu['03'] = 'Vidas Estaticas'
        menu['04'] = 'Guardar juego'
        menu['05'] = 'Cargar juego'
        menu['06'] = 'Salir del sistema'

        while True:
            try:
                os.system('clear')
                for k in sorted(menu):
                    print (str(k) + ' ' + menu[k])
                if self.juego.started or not self.juego.modo: selection = input('Elija un opción: ')

                # Patron random
                if selection == '1' or selection == '01':
                    if self.juego.started:
                        ans = input('Ya hay un juego empezado, si continuas se perdera. Continuar? S/N: ')
                        if ans == 's' or ans == 'S':
                            self.juego = juego_de_la_vida([])
                        elif ans == 'N' or ans == 'n':
                            continue
                        else:
                            print('opcion no valida, abortando...')
                            time.sleep(1)
                            continue
                    self.juego.modo = 1
                    rows, columns = self.juego.prepare_game()
                    cells = int(input('Numero de celulas vivas: '))
                    table = [(x, y) for x in range(rows) for y in range(columns)]
                    shuffle(table)
                    patron = (table[:cells])
                    self.juego.game(rows, columns, patron)

                # Seleccion ubicacion de celdas
                elif selection == '2' or selection == '02':
                    if self.juego.started:
                        ans = input('Ya hay un juego empezado, si continuas se perdera. Continuar? S/N: ')
                        if ans == 's' or ans == 'S':
                            self.juego = juego_de_la_vida([])
                        elif ans == 'N' or ans == 'n':
                            continue
                        else:
                            print('opcion no valida, abortando...')
                            time.sleep(1)
                            continue
                    self.juego.modo = 2
                    rows, columns = self.juego.prepare_game()
                    cells = int(input('Numero de celulas vivas: '))
                    if not self.control.cells_max_matriz(cells, rows, columns):
                        patron = [[0 for x in range(rows)] for y in range(columns)]
                        count = 0
                        while (count < cells):
                            row, column = (int(input('ubicacion de fila: ')) , int(input('ubicacion de columna : ')))
                            # controlar vivas repetidas y que no se salga de rango
                            if self.control.control_ubicacion_disponible(row, column, patron):
                                patron[row][column] = 1
                                self.juego.paintTable(patron , rows , columns)  # print como va quedando la matriz
                                count = count + 1
                        self.juego.actualTable = patron
                        self.juego.game(rows, columns, self.juego.actualTable)

                # Opcion 3
                elif selection == '3' or selection == '03':
                    pass
                # opcion 4
                elif selection == '4' or selection == '04':
                    tablero = self.juego.futureTable
                    archivo = input('ingrese el nombre del archivo sin extension:  ')
                    pickle.dump(tablero, open(archivo,'wb'))
                    data = {}
                    data['modo'] = self.juego.modo
                    data['rows'] = len(tablero)
                    data['columns'] = len(tablero[0])
                    json.dump(data, open(archivo + '-data.json', 'w'))


                elif selection == '5' or selection == '05':
                    archivo = input('ingrese el nombre del archivo a cargar sin extension: ')
                    self.juego.actualTable = pickle.load(open(archivo, 'rb'))
                    data = json.load(open(archivo + '-data.json', 'rb'))
                    self.juego.modo = data['modo']
                    self.juego.game(data['rows'], data['columns'], self.juego.actualTable)

                # Salir
                elif selection == '6' or selection == '06':
                    "Gracias por jugar al juego de la vida..."
                    time.sleep(1)
                    break
                else:
                    print(40 * '-')
                    print ('Opcion invalida')
                    print(40 * '-')
                    time.sleep(1)

            except (EOFError, KeyboardInterrupt):
                    print(' ')
                    print(40 * '-')
                    print ('Para Salir elija la opcion 05')
                    print(40 * '-')
                    time.sleep(1)



if __name__ == '__main__':
    print('Iniciando juego..')
    menu()
