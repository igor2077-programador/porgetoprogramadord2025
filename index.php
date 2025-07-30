<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>teste php</title>
</head>
<body>
    <?php
        $nome='JHONAs';
        if($nome=='JHONAS'){
            echo" e o jhonas";
        }else{
            echo"e um imposor";
        }

        echo"<h1> ola mundo! bem-vendo(a) $nome </h1>";

        $idade = 17;
        if($idade >= 16){
            echo'<br> pode votar!';
        }else{
            echo'<br>nao pode votar!';
        }

        for($contador=0; $contador <10; $contador++){
            echo'<hr><img src="https://www.moneyreport.com.br/wp-content/uploads/2022/05/alexandre-de-moraes-1024x682.jpg">';
            echo $contador;
        }

        $numero=0;
        while($numero < 10){
            echo"<br> item da lista numero $numero";
            $numero=$numero+1;
        }
    ?>
</body>
</html>