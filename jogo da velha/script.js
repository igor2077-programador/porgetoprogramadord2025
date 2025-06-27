var jogador="x"

function jogar(celula){
    if(celula.innerHTML =="")
        celula.innerHTML = jogador;
    if(jogador =="x"){
        jogador = "o"
        celula.stayle
    } 
    else{
        jogador = "x"
    }
   
}
 function reiniciar(){
    window.location.reload()}