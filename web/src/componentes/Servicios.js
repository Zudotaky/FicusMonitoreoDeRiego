const fetch = require('node-fetch');
let urlBase = "http://192.168.100.236:5000"
urlBase = "http://localhost:5000"

class Servicios {

    obtenerEspacios(){
        const url = new URL("/Espacio/obtenerEspacios", urlBase).toString();
        
        return fetch(url).then(res => res.json()).then(({ Espacios }) => Espacios)
    }
}

export default Servicios;
