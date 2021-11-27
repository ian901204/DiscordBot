<?php
//Input your sql information
$servername = "";
$serverusername = "";
$serverpassword = "";
$db="";
$conn = mysqli_connect($servername, $serverusername, $serverpassword,$db);
mysqli_set_charset($conn, "UTF8");
// Check connection
if (!$conn){
    die("Connection failed: " . mysqli_connect_error());
}

?>
