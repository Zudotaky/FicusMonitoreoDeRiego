from flask_restplus import Api

api = Api(version='1.0', title='Ficus', description='APi Ficus',)

from Api.ApiPlanta import plantasRequest
api.add_namespace(plantasRequest)

from Api.ApiEspacio import espacioRequest
api.add_namespace(espacioRequest)

from Api.ApiRegistro import registroRequest
api.add_namespace(registroRequest)