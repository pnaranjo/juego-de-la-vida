#!/usr/bin/python3
# Version 1.0

import os

menu = {}
menu['01']="Patron random"
menu['02']="Selecciar ubicacion inicial"
menu['03']="Avanzar paso a paso"
menu['04']="Avance automatico"
menu['05']="Salir del sistema"


while True:
    try:
        os.system('clear')
        for k in sorted(menu):
                print (str(k) + ' ' + menu[k])
        print()
        selection = input("Elija un opción: ")

        if selection == '1' or selection == '01':
             pass
        elif selection == '2' or selection == '02':
             pass
        elif selection == '3' or selection == '03':
             pass
        elif selection == '4' or selection == '04':
             pass
        elif selection == '5' or selection == '05':
             break
        else:
            print(40 * '-')
            print ("Opcion invalida")
            print(40 * '-')
    except (EOFError, KeyboardInterrupt):
            print(40 * '-')
            print ("Para Salir elija la opcion 05")
            print(40 * '-')
