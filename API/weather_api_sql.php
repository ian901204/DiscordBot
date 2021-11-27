<?php
require("sql_conn.php");
ini_set('display_errors', 1);
echo __DIR__;
$weather=[];
$city=[["taipei","台北"],["keelung","基隆"],["Taitung","台東"],["Pingtung","屏東"],["Yilan","宜蘭"],["Tainan","台南"],['Kaohsiung','高雄']];
$sql_delete="DELETE FROM weather";
if ($conn->query($sql_delete) == TRUE) {
      foreach($city as $cityname){
            $string = file_get_contents("https://api.openweathermap.org/data/2.5/weather?q=".$cityname[0]."&appid=Your API key&lang=zh_tw&units=metric");
            //$string= file_get_contents(__DIR__."/test.json");
            $json_a = json_decode($string, true);
            $location = $cityname[1];
            $maxtemp = $json_a["main"]["temp_max"];
            $mintemp = $json_a["main"]["temp_min"];
            $description = urldecode(urlencode($json_a["weather"][0]["description"]));
            $sunrise = $json_a["sys"]["sunrise"];
            $sunrise = urldecode(urlencode(date("H:i",$sunrise+28800)));
            $sunset = $json_a["sys"]["sunset"];
            $sunset = urldecode(urlencode(date("H:i",$sunset+28800)));
            $updateTime = date("Y-m-d H:i:s",time()+28800);
            $sql = "INSERT INTO weather(location, maxtemp, mintemp, description, sunrise_time, sunset_time, updateTime) VALUES ('$location', '$maxtemp', '$mintemp', '$description', '$sunrise', '$sunset', '$updateTime')";
            if ($conn->query($sql) == TRUE){
            }else{
                  echo("Error description: " . $conn -> error."<br>");
            }
      }
}
?>
