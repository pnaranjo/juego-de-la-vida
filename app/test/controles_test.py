#!/usr/bin/env python3
import unittest
#NO ME ESTA TOMANDO EL IMPORT
from juego_de_la_vida.app.controles import matriz_minima

class ControlesTests(unittest.TestCase):

    def test_matriz_minima(self):
        self.assertEquals(matriz_minima(3,3),True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
