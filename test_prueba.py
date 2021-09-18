from unittest import TestCase, skip
from prueba import sumatoria


class TestPruebas(TestCase):
    @skip('Demostrando los test, no sirve este test')
    def testPrueba(self):
        x = 11
        self.assertEqual(x, 10)

    def testSumatoria(self):
        resultado = sumatoria(5,6)
        self.assertEqual(resultado, 11)
        self.assertNotEqual(resultado,10)
        
