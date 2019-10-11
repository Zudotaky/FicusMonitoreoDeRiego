from flask_restplus import Api

api = Api(version='1.0', title='Ficus', description='APi Ficus',)

from backend.Phyton.Api.ApiPlanta import plantasRequest
api.add_namespace(plantasRequest)

from backend.Phyton.Api.ApiEspacio import espacioRequest
api.add_namespace(espacioRequest)

from backend.Phyton.Api.ApiRegistro import registroRequest
api.add_namespace(registroRequest)