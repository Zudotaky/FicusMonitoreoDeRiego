import { callToServer } from './callToServer'

//////ESPACIO
class EspaciosServ {
  async obtenerEspacios() {
    return await callToServer('GET', '/Espacio/obtenerEspacios')
  }
}

export default EspaciosServ
