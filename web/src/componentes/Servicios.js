const fetch = require('node-fetch');
let urlBase = "http://192.168.100.236:5000"
urlBase = "http://localhost:5000"

class Servicios {

    obtenerEspacios(){
        const url = new URL("/Espacio/obtenerEspacios", urlBase).toString();
        
        return fetch(url).then(res => res.json()).then(({ Espacios }) => Espacios)
    }

    obtenerPlantas(idEspacio){
        const url = new URL("/Plantas/ObtenerPorEspaioId", urlBase).toString();

        return fetch(url, {
            method: 'POST',
            body: JSON.stringify({idEspacio}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(({ Plantas }) => Plantas)
    }

    obtenerDataChart(idPlanta){
        const url = new URL("/Registro/obtenerSensosPorId", urlBase).toString();

        return [
            {humedad: 7, fecha: '23:11:22 04/02/2000'},
            {humedad: 666, fecha: '23:11:22 04/02/2001'},
            {humedad: 1023, fecha: '23:11:22 04/02/2002'}
        ]
        /*
        return fetch(url, {
            method: 'POST',
            body: JSON.stringify({id: idPlanta}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(({Registros}) => Registros)
    */
    }
}

export default Servicios;
