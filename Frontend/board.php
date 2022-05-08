<?php
require "auth.php";
$service_url = 'http://m242mqtt.azurewebsites.net/api/get_sensors';

$curl = curl_init($service_url);
curl_setopt($curl, CURLOPT_USERPWD, $_SESSION['username'] . ":" . $_SESSION['password']);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$output=curl_exec($curl);
$result = json_decode($output, 1);
curl_close($curl);

$temperature = $result["temperature"];
$humidity = $result["humidity"];
?>

<!DOCTYPE html>
<html>

<head>
    <title>IotKitv3 Sensors</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>



<body>
    <main>
        <div class="TitleBoxIotKit">
            <h1><?php echo $_SESSION['username']; ?>'s IotKitv3</h1>
        </div>
        <div class="Sensors">
            <table>
                <tr>
                    <td>Temperature:</td>
                    <td><?php echo $temperature; ?></td>
                </tr>
                <tr>
                    <td>Humidity:</td>
                    <td><?php echo $humidity; ?></td>
                </tr>
            </table>
        </div>

        <form action="logout.php" method="POST" class="Logout">
            <input type="submit" class="LogoutButton" value="Logout">
        </form>
    </main>
</body>

</html>