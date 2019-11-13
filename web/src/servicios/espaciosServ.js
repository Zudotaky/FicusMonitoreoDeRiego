import { callToServer } from './callToServer'

//////ESPACIO
class EspaciosServ {
  async obtenerEspacios() {
    return await callToServer('GET', '/Espacio/obtenerEspacios').then(({ Espacios }) => Espacios)
  }
}

export default EspaciosServ
