import unittest
from src.logica.conjunto import

class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
            self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento( self ):
        conjunto=Conjunto([1])
            self.assertEqual(5,conjunto.promedio())
