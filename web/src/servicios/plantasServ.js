///////////PLANTA 
const fetch = require('node-fetch')
let urlBase = 'http://192.168.100.236:5000'
urlBase = 'http://localhost:5000'

class plantasServ {

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
}

export default plantasServ
