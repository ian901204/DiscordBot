<?php
require("sql_conn.php");
$weather=array();
$sql="SELECT * FROM weather";
$result=$conn->query($sql);
$updateTime="";
while($row=mysqli_fetch_array($result)){
	if($updateTime == "" ){
		$updateTime = $row["updateTime"];
	}
 array_push($weather,["des"=>$row['description'],"name"=>$row['location'],"maxtemp"=>$row['maxtemp'],"mintemp"=>$row['mintemp'],"sunrise"=>$row['sunrise_time'],"sunset"=>$row['sunset_time'],"updateTime"=>""]);
}
array_push($weather,["updateTime" => $updateTime]);
header('Content-Type: application/json');
echo json_encode($weather);
?>