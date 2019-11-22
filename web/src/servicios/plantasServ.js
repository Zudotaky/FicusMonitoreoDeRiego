import { callToServer } from './callToServer'

///////////PLANTA 


class plantasServ {

    async obtenerPlantas(idEspacio) {
        return await callToServer('POST', '/Plantas/ObtenerPorEspaioId', {idEspacio: idEspacio}).then(({ Plantas }) => Plantas)
    }
}

export default plantasServ
