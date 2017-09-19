import unittest
from app.controles import controles


class ControlesTests(unittest.TestCase):

    def test_matriz_minima(self):
        self.assertTrue(controles.matriz_minima(3,3),'True')

    def test_cells_max_matriz(self):
        self.assertFalse(controles.cells_max_matriz(8, 3, 3),'False')

    def test_cells_max_matriz_f(self):
        self.assertTrue(controles.cells_max_matriz(10, 3, 3), 'True')

    def test_ubicacion_disponible(self):
        patron = [[0 for x in range(3)] for y in range(3)]
        self.assertTrue(controles.control_ubicacion_disponible(1, 1, patron), 'True')

    def test_ubicacion_disponible_repetido(self):
        patron = [[0 for x in range(3)] for y in range(3)]
        patron[1][1]=1
        self.assertFalse(controles.control_ubicacion_disponible(1, 1, patron), 'False')

    def test_ubicacion_disponible_fuera_de_limite(self):
        patron = [[0 for x in range(3)] for y in range(3)]
        self.assertFalse(controles.control_ubicacion_disponible(5, 5, patron), 'False')

    def ControlesTests(self):
        unittest.main()

if __name__ == '__main__':
    ControlesTests()
