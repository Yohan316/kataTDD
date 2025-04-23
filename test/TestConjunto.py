import unittest
from src.logica.conjunto import

class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
            self.assertIsNone(conjunto.promedio())


if __name__ == '__main__':
    unittest.main()
