import { callToServer } from './callToServer'

//////////////REGISTRO

class RegistrosServ {

    async obtenerDataChart(idPlanta) {
        return await callToServer('POST', '/Registro/obtenerSensosPorId', {id: idPlanta})
    }

    async obtenerUltimoSenso(idPlanta){
        return await callToServer('POST', '/Registro/obtenerUltimo', {id: idPlanta})
    }
}

export default RegistrosServ
