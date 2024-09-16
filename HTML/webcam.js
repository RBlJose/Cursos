var altoCamara = 720;
var anchoCamara = 720;

var amarillo = {r: 255, g: 255, b: 0};

var distanciaAceptable = 175;

function mostrarCamara(){
    var video = document.getElementById("video");
    var canvas = document.getElementById("canvas");

   var opciones = {
       audio: false,
       video: {
           width: altoCamara, height: anchoCamara
       }
   };

    if (navigator.mediaDevices.getUserMedia){
       navigator.mediaDevices.getUserMedia(opciones)
           .then(function(stream){
               video.srcObject = stream;
               procesarCamara();
           })
           .catch(function(err){
               console.log("Oops, hubo un error", err);
           })
   } else {
       console.log("No existe la funcion getUserMedia... oops :(");
   }
}



function procesarCamara(){

    var ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, anchoCamara, altoCamara, 0, 0, canvas.width, canvas.height);

    var imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    var pixeles = imgData.data;
    //var menorDistancia = null;
    /*var sumaX = 0;
    var sumaY = 0;
    var cuenta = 0;*/

    var platanetes = [];

    for ( var p=0; p<pixeles.length; p +=4){
        var rojo = pixeles[p];
        var verde = pixeles[p+1];
        var azul = pixeles[p+2];
        var alpha = pixeles[p+3];
        var distancia = Math.sqrt(
            Math.pow(amarillo.r-rojo, 2)+
            Math.pow(amarillo.g-verde, 2)+
            Math.pow(amarillo.b-azul, 2)    
            );

        if (distancia < distanciaAceptable) {
            /*pixeles[p] = 255;
            pixeles[p+1] = 0;
            pixeles[p+2] = 0;*/

            var y = Math.floor(p / 4 / canvas.width);
            var x = (p/4) % canvas.width;
            
            
            if (platanetes.length == 0) {
                var platanete = new Platanete(x, y);
                platanetes.push(platanete);
            } else {
                var encontrado = false;
                for (var pl=0; pl < platanetes.length; pl++) {
                    if (platanetes[pl].estaCerca(x, y)) {
                            platanetes[pl].agregarpixel(x, y);
                            encontrado = true;
                            break;
                    }
                }

                if (!encontrado) {
                    var platanete = new Platanete(x, y);
                    platanetes.push(platanete);
                }
            }

           /* sumaX += x;
            sumaY += y;
            cuenta ++;*/

        /*if (menorDistancia == null || distancia < menorDistancia) {
            menorDistancia = distancia;

            

            pixelmasAmarillo = {x: x, y: y};
        }*/
        }
    }

    ctx.putImageData(imgData, 0, 0)

    for ( var pl= 0; pl < platanetes.length; pl++) {
        platanetes[pl].dibujar(ctx);
    }

    /*if (cuenta > 0) {
        ctx.fillStyle = '#00f';
        ctx.beginPath();
        ctx.arc(sumaX/cuenta, sumaY/cuenta, 10, 0, 2*Math.PI);
        ctx.fill();
    }*/
   setTimeout(procesarCamara, 20);
}