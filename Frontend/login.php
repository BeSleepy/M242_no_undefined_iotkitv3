<!DOCTYPE html>
<html>

    <head>
        <title>IoTKitv3 Login</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>

    <body>
        <main>
            <div class="TitleBox">
                <h1>IoTKitv3 Login</h1>
            </div>

<?php
session_start();
$service_url = 'https://m242mqtt.azurewebsites.net/login';

if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == true) {
    header("Location: board.php");
}

if (isset($_POST["username"]) && isset($_POST["password"])) {
    
    $username = $_POST["username"];
    $password = $_POST["password"];

    if($username !== "" && $password !== ""){
            
        $body = [
                'username' => $username,
                'password' => $password
        ];
        $ch = curl_init();

        curl_setopt($ch,CURLOPT_URL, $service_url);
        curl_setopt($ch,CURLOPT_POST, true);
        curl_setopt($ch,CURLOPT_POSTFIELDS, $body);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
        
        $result = curl_exec($ch);
        if (!curl_errno($ch)) {
            curl_close($ch);

            $result = json_decode($result, True);
            $array_result = array_values($result);
            if($array_result[0] === "True") {
                    $_SESSION['loggedin'] = true;
                    $_SESSION['username'] = $username;
                    $_SESSION['password'] = $password;
                    header("Location:board.php");
            }
            else{
                echo "<h2 style=\"color: red\"> Login failed. Please scan card and then provide valid login credentials!</h2>";
            }
        }
        else{
            echo "<h2> Curl failed. Contact site administrator!</h2>";
        }
    }
}
    
?>

            <div class="FormBox">
                <form action="login.php" method="POST">
                    <table>
                        <tr>
                            <td>Username:</td>
                            <td>
                                <input type="text" name="username" class="Textfield">
                            </td>
                        </tr>
                        <tr>
                            <td>Password:</td>
                            <td>
                                <input type="password" name="password" class="Textfield">
                            </td>
                        </tr>
                        <tr>
                            <td id="Login">
                                <input type="submit" class="SubmitButton" value="Login">
                            </td>
                        </tr>

                    </table>
                </form>
            </div>

        </main>
    </body>
</html>