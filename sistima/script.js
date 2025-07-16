let table = new DataTable('#tabela', {
   language: {
        url: 'https://cdn.datatables.net/plug-ins/2.3.2/i18n/pt-BR.json',
    },  
});
function visualizar(){
    var senha=$('#senha')
    var icone=$('#olho')

    if(senha.attr('type')==='password'){
        senha.attr('type','text');
        icone.removeClass('fa-eye').addClass('fa-eye-slash')
    }
    else{
        senha.attr('type','password');
        icone.removeClass('fa-eye-slash').addClass('fa-eye');
    }
}

