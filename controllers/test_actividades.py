from app import app
from unittest import TestCase

class TestActividadesController(TestCase):
    def setUp(self):
        '''Es el metodo que servira apara configurar mis  test de esta clase'''
        self.app = app.test_client()

    def test_get_actividades(self):
        respuesta = self.app.get('/actividades')
       
        self.assertEqual(respuesta.json, dict(message=None, content=[{ 
            
                "actividadID": 1,
                "actividadNombre": "Ir a la playa"
            },
                {
                "actividad": 2,
                "actividadNombre": "Cocinar"
            },
                {
                "actividad": 3,
                "actividadNombre": "Ir al cumpleaños de mi abuela"

            }]))

        self.assertEqual(respuesta.status_code, 201)

    def test_fail_post_actividades(self):
        respuesta = self.app.post('/actividades')

        self.assertEqual(respuesta.status_code, 400)
        self.assertDictEqual(respuesta.json, dict(
            message={'actividadNombre': 'Falta la actividadNombre'}))

    def test_post_actividades(self):
        respuesta = self.app.post('/actividades', json={'actividadNombre': 'Hacer la tarea de backend'})

        self.assertEqual(respuesta.status_code, 201)
        self.assertIsNotNone(respuesta.json)
