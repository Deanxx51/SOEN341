<?php
include_once("connect.php");

$ip = get_client_ip();
$id = $_POST['id'];
if(!isset($id) || empty($id)) exit;

$ip_sql=mysql_query("select ip from pic_ip1 where pic_id='$id' and ip='$ip'");
$count=mysql_num_rows($ip_sql);
if($count==0){
	$sql = "update pic1 set unlove=unlove+1 where id='$id'";
	mysql_query( $sql);
	$sql_in = "insert into pic_ip1 (pic_id,ip) values ('$id','$ip')";
	mysql_query( $sql_in);
	$result = mysql_query("select unlove from pic1 where id='$id'");
	$row = mysql_fetch_array($result);
	$unlove = $row['unlove'];
	echo $unlove;
}else{
	echo "You have already voted";
}

//get user's IP address
function get_client_ip() {
	if (getenv("HTTP_CLIENT_IP") && strcasecmp(getenv("HTTP_CLIENT_IP"), "unknown"))
		$ip = getenv("HTTP_CLIENT_IP");
	else
		if (getenv("HTTP_X_FORWARDED_FOR") && strcasecmp(getenv("HTTP_X_FORWARDED_FOR"), "unknown"))
			$ip = getenv("HTTP_X_FORWARDED_FOR");
		else
			if (getenv("REMOTE_ADDR") && strcasecmp(getenv("REMOTE_ADDR"), "unknown"))
				$ip = getenv("REMOTE_ADDR");
			else
				if (isset ($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], "unknown"))
					$ip = $_SERVER['REMOTE_ADDR'];
				else
					$ip = "unknown";
	return ($ip);
}
?>