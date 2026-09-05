<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>aula06_02.php</title>
</head>
<body>
    <h1> Aula06_02-11/09/25</h1>
    <?php
    echo"<pre>";print_r($_REQUEST);echo"</pre>";
    $login=$POST["login"];
    $senha=$POST["senha"];
    echo "login: $login<br>";
    echo "senha: $senha<br>";
    ?>
</body>
</html>