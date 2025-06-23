
var celular = document.querySelector('.celular');     //icone de menu
var listaMenu = document.querySelector('.menu ul');   //itens do menu

celular.addEventListener('click', function(){ 
    listaMenu.classList.toggle('mostrarMenu');
 });
 
