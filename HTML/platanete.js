class Platanete {
    pixeles = [];

    xMin = 0;
    xMax = 0;
    yMin = 0;
    yMax = 0;

    constructor(x, y){
        this.agregarpixel(x, y);
        this.xMin = x;
        this.xMax = x;
        this.yMin = y;
        this.yMax = y;
    }

    agregarpixel(x, y) {
        this.pixeles.push({x: x, y: y});

        this.xMin = x < this.xMin ? x : this.xMin;
        this.xMax = x > this.xMax ? x : this.xMax;
        this.yMin = y < this.yMin ? y : this.yMin;
		this.yMax = y > this.yMax ? y : this.yMax;
    }
    estaCerca (x, y) {
        var menorDistancia = -1;
        for(var p=0; p < this.pixeles.length; p++) {
            var distancia = Math.sqrt(

                Math.pow(this.pixeles[p].x-x, 2)+
                Math.pow(this.pixeles[p].y-y, 2)               
                );

                if (menorDistancia == -1 || distancia < menorDistancia){
                    menorDistancia = distancia;
                }
        
        if (menorDistancia <= 100 ){
            return true
        }

        return false;
        
        }
    }
    dibujar(ctx) {
        ctx.strokeStyle = '#f00';
        ctx.lineWidth = 4;
        ctx.beginPath();
        var x = this.xMin;
        var y = this.yMin;
        var width = this.xMax - this.xMin;
        var height = this.yMax - this.yMin;

        ctx.rect(x, y, width, height);
        ctx.stroke();
    }
    
    
}