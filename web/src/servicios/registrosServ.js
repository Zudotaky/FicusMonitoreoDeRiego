//////////////REGISTRO

const fetch = require('node-fetch')
let urlBase = 'http://192.168.100.236:5000'
urlBase = 'http://localhost:5000'

class resgistrosServ {

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

    async obtenerUltimoSenso(idPlanta){
        const url = new URL('/Registro/obtenerUltimo', urlBase).toString()

        // return fetch(url, {
        //     method: 'POST',
        //     body: JSON.stringify({id: idPlanta}),
        //     headers: {
        //         'Content-Type': 'application/json'
        //     }
        // }).then(res => res.json()).then(({ Senso }) => Senso)
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify({id: idPlanta}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const ultimoSenso = await response.json()
        console.log('log de sensos:', ultimoSenso)
        return ultimoSenso
    }
}

export default resgistrosServ
