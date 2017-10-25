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
                pdb.set_trace()
                if self.juego.started or not self.juego.modo:
                    selection = input('Elija un opción: ')
                else:
                    selection = self.juego.modo



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
                    cells = input('Numero de celulas vivas: ')
                    if not self.control.verify_input_int(cells,0):
                        not_int = True
                        while not_int:
                            cells = input('Numero de celulas vivas: ')
                            not_int = not self.control.verify_input_int(cells,0)
                    table = [(x, y) for x in range(rows) for y in range(columns)]
                    shuffle(table)
                    patron = (table[:int(cells)])
                    self.juego.game(rows, columns, patron)

                # Seleccion ubicacion de celdas
                elif selection == '2' or selection == '02':
                    if self.juego.started:
                        ans = str(input('Ya hay un juego empezado, si continuas se perdera. Continuar? S/N: '))
                        if ans.upper() == 'S':
                            self.juego = juego_de_la_vida([])
                        elif ans.upper() == 'N':
                            continue
                        else:
                            print('opcion no valida, abortando...')
                            time.sleep(1)
                            continue
                    self.juego.modo = 2
                    rows, columns = self.juego.prepare_game()
                    cells = input('Numero de celulas vivas: ')
                    if not self.control.verify_input_int(cells,0):
                        not_int = True
                        while not_int:
                            cells = input('Numero de celulas vivas: ')
                            not_int = not self.control.verify_input_int(cells,0)
                    if not self.control.cells_max_matriz(int(cells), rows, columns):
                        patron = [[0 for x in range(rows)] for y in range(columns)]
                        count = 0
                        while (count < int(cells)):
                            row, column = (input('ubicacion de fila: ') , input('ubicacion de columna : '))
                            if not self.control.verify_input_int(row,column):
                                not_int = True
                                while not_int:
                                    row, column = (input('ubicacion de fila: ') , input('ubicacion de columna : '))
                                    not_int = not self.control.verify_input_int(row,column)
                            if self.control.control_ubicacion_disponible(int(row), int(column), patron):
                                patron[int(row)][int(column)] = 1
                                self.juego.paintTable(patron , rows , columns)  # print como va quedando la matriz
                                count = count + 1
                        self.juego.actualTable = patron
                        self.juego.game(rows, columns, self.juego.actualTable)

                # Opcion 3
                elif selection == '3' or selection == '03':
                    self.juego.modo = 3
                    if self.juego.started:
                        ans = str(input('Ya hay un juego empezado, si continuas se perdera. Continuar? S/N: '))
                        if ans.upper() == 'S':
                            self.juego = juego_de_la_vida([])
                        elif ans.upper() == 'N':
                            continue
                        else:
                            print('opcion no valida, abortando...')
                            time.sleep(1)
                            continue
                    rows, columns = self.juego.prepare_game()
                    cells = input('Numero de celulas vivas: ')
                    self.juego.vidas_estaticas(rows, columns, int(cells))

                # opcion 4
                elif selection == '4' or selection == '04':
                    if not self.juego.started:
                        print('Debe iniciar el juego primero')
                        time.sleep(2)
                    else:
                        tablero = self.juego.futureTable
                        archivo = input('ingrese el nombre del archivo sin extension:  ')
                        pickle.dump(tablero, open(archivo,'wb'))
                        data = {}
                        data['modo'] = self.juego.modo
                        if self.juego.modo == 3:
                            data['cells'] = cells
                            data['contador_estatico'] = self.juego.contador_estatico
                            data['cantidad'] = self.juego.cantidad
                            pickle.dump(list(self.juego.iter_list_x), open(archivo + '-vex', 'wb'))
                            pickle.dump(list(self.juego.iter_list_y), open(archivo + '-vey', 'wb'))
                        data['modo_f'] = self.juego.modo_f
                        data['rows'] = len(tablero)
                        data['columns'] = len(tablero[0])
                        json.dump(data, open(archivo + '-data.json', 'w'))

                # Opcion 5
                elif selection == '5' or selection == '05':
                    try:
                        archivo = input('ingrese el nombre del archivo a cargar sin extension: ')
                        self.juego.actualTable = pickle.load(open(archivo, 'rb'))
                        data = json.load(open(archivo + '-data.json', 'r'))
                        self.juego.modo = data['modo']
                        self.juego.modo_f = data['modo_f']
                        if self.juego.modo == 3:
                            self.juego.iter_list_x = pickle.load(open(archivo + '-vex', 'rb'))
                            self.juego.iter_list_y = pickle.load(open(archivo + '-vey', 'rb'))
                            self.juego.vidas_estaticas(data['rows'], data['columns'], data['cells'], data['cantidad'], data['contador_estatico'])
                        else:
                            self.juego.game(data['rows'], data['columns'], self.juego.actualTable)
                    except OSError:
                        print('*** Archivo no encontrado ***')
                        time.sleep(2)
                # Salir
                elif selection == '6' or selection == '06':
                    print("Gracias por jugar al juego de la vida...")
                    time.sleep(1)
                    break

                #Cualquier otro ingreso
                else:

                    print(40 * '-')
                    print ('Opcion invalida')
                    print(40 * '-')
                    time.sleep(1)

            except (EOFError, KeyboardInterrupt):

                    selection = None
                    self.juego.modo = None
                    print(' ')
                    print(40 * '-')
                    print ('Para Salir elija la opcion 06')
                    print(40 * '-')
                    time.sleep(1)



if __name__ == '__main__':
    print('Iniciando juego..')
    menu()
