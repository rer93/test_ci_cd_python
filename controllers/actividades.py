from flask_restful import Resource, reqparse

class ActividadesController(Resource):
    def get(self):
        return {
            "message": None,
            "content": [{
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

            }]
        }, 201