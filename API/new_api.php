<?php
require("sql_conn.php");
ini_set('display_errors','1');
$sql="SELECT * FROM news";
$re=$conn->query($sql);
$data=array();
while($row=mysqli_fetch_array($re)){
 $url_data=["url"=>$row["url"],"updateTime"=>$row["updateTime"]];
 array_push($data, $url_data);
}
	header('Content-Type: application/json');
	echo json_encode($data);
?>