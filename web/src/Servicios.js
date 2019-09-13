class Servicios {

    obtenerAlgo(){
        var ourRequest = new XMLHttpRequest();
        ourRequest.open('GET','https://learnwebcode.github.io/json-example/animals-1.json');
        ourRequest.onload = function () {
            var ourData = JSON.parse(ourRequest.responseText);
            console.log(ourData);
        };
        ourRequest.send();
    }

    obtenerSensos(idPlanta, fechaInicio, fechaFin){
        var xhr = new XMLHttpRequest();
        var url = "url";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-type", "application/json");

        xhr.onreadystatechange = function () { 
            if (xhr.readyState == 4 && xhr.status == 200) {
                var json = JSON.parse(xhr.responseText);
                console.log(json);
            }
        }
        var data = JSON.stringify({"idPlanta": idPlanta,"fechaInicio":fechaInicio, "fechaFin": fechaFin});
        xhr.send(data);

    }

    obtenerHumedadDeEntre(idPlanta, fechaInicio, fechaFin) {
        return this.obtenerSensos(idPlanta,fechaInicio, fechaFin);
    }

}
 /*let spo = new Servicios();
 spo.populateAlbumsForArtist("Gorillaz");*/

export default Servicios;
