from flask_restful import Resource, reqparse

serializador = reqparse.RequestParser(bundle_errors=True)
serializador.add_argument(
    'actividadNombre',
    required=True,
    location='json',
    help='Falta la actividadNombre',
    type=str
)

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

    def post(self):
        data = serializador.parse_args()
        # logica para resgistrar la actividad en la bd
        actividadCreada = {
            "actividadId": 50,
            "actividadNombre": data.get('actividadNombre')
        }
        return {
            "message": "actividad creada exitosamente",
            "content": actividadCreada
        }, 201