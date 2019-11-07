const fetch = require('node-fetch')
let urlBase = 'http://192.168.100.236:5000'
urlBase = 'http://localhost:5000'

class Servicios {

    obtenerEspacios(){
        const url = new URL('/Espacio/obtenerEspacios', urlBase).toString()
        
        return fetch(url).then(res => res.json()).then(({ Espacios }) => Espacios)
    }

    obtenerPlantas(idEspacio){
        //if (!idEspacio) {return []}
        const url = new URL('/Plantas/ObtenerPorEspaioId', urlBase).toString()

        return fetch(url, {
            method: 'POST',
            body: JSON.stringify({idEspacio}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(({ Plantas }) => Plantas)
    }

    async obtenerDataChart(idPlanta){
        const url = new URL('/Registro/obtenerSensosPorId', urlBase).toString()

        // return [
        //     {uv: 7, name: '23:11:22 04/02/2000'},
        //     {uv: 666, name: '23:11:22 04/02/2001'},
        //     {uv: 1023, name: '23:11:22 04/02/2002'}
        // ]
        
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify({id: idPlanta}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const registros = await response.json()
        // const registros = json.Registros.map(datos => {
        //     datos.name = datos.fecha
        //     datos.uv = datos.humedad
        //     return datos
        // })
        console.log('se llamo el servicio para obtener sensos')
        console.log(registros)
        return registros
    }
}

export default Servicios
