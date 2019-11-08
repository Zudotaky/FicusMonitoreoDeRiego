const fetch = require('node-fetch')
let urlBase = 'http://192.168.100.236:5000'
urlBase = 'http://localhost:5000'

class Servicios {

    obtenerEspacios(){
        const url = new URL('/Espacio/obtenerEspacios', urlBase).toString()
        
        return fetch(url).then(res => res.json()).then(({ Espacios }) => Espacios)
    }

    obtenerPlantas(idEspacio){
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
        
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify({id: idPlanta}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const registros = await response.json()
        return registros
    }

    obtenerUltimoSenso(idPlanta){
        const url = new URL('/Registro/obtenerUltimo', urlBase).toString()

        return fetch(url, {
            method: 'POST',
            body: JSON.stringify({id: idPlanta}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(({ Senso }) => Senso)
    }
}

export default Servicios
