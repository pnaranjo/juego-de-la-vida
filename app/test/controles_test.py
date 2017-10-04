#!/usr/bin/env python3
import unittest
from app.controles import controles


class ControlesTests(unittest.TestCase):
    control = controles()

    def test_matriz_minima_t(self):
        self.assertTrue(self.control.matriz_minima(3,3),'True')

    def test_matriz_minima_f(self):
        self.assertFalse(self.control.matriz_minima(1,3),'False')

    def test_cells_max_matriz(self):
        self.assertFalse(self.control.cells_max_matriz(8, 3, 3),'False')

    #Arreglarlo espera un input    
    #def test_cells_max_matriz_f(self):
    #   self.assertTrue(self.control.cells_max_matriz(10, 3, 3), 'True')

    def test_ubicacion_disponible(self):
        patron = [[0 for x in range(3)] for y in range(3)]
        self.assertTrue(self.control.control_ubicacion_disponible(1, 1, patron), 'True')

    def test_ubicacion_disponible_repetido(self):
        patron = [[0 for x in range(3)] for y in range(3)]
        patron[1][1]=1
        self.assertFalse(self.control.control_ubicacion_disponible(1, 1, patron), 'False')

    def test_ubicacion_disponible_fuera_de_limite(self):
        patron = [[0 for x in range(3)] for y in range(3)]
        self.assertFalse(self.control.control_ubicacion_disponible(5, 5, patron), 'False')

    def test_solo_enteros_t(self):
        self.assertTrue(self.control.verify_input_int(10, 9),'True')

    def test_solo_enteros_f(self):
        self.assertFalse(self.control.verify_input_int(10, 'L'),'False')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
