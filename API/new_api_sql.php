<?php
require("sql_conn.php");
ini_set('display_errors','1');
$sql="DELETE FROM news";
if ($conn->query($sql) ==TRUE){
	$string = file_get_contents("http://newsapi.org/v2/top-headlines?country=tw&apiKey=Your API key");
  $json_a = json_decode($string,true);
  foreach ($json_a["articles"] as $key ){
  $url=$key["url"];
  $updateTime = date("Y-m-d H:i:s",time()+28800);
  $sql="INSERT INTO news (url,updateTime) VALUES('$url', '$updateTime')";
  if ($conn->query($sql) != TRUE){
    echo $url;
  }else{
  }
  } 
}