const fetch = require('node-fetch');
let urlBase = "http://192.168.100.236:5000"

class Servicios {

    async obtenerEspacios(){
        
        let url = urlBase + "/Espacio/obtenerEspacios";
        url = "https://jsonplaceholder.typicode.com/todos/1"
        let response = await fetch(url).catch((error) => {console.log('pepepe',error)})
        let espacios = await response.json()
        console.log("espaciosssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        console.log(espacios)
        return espacios;

    }
}
//let serv = new Servicios();
//serv.obtenerEspacios();

export default Servicios;
