<html>
 <head>
  <title>PHP Test</title>
  <script type="text/javascript" src="jquery.min.js"></script>
<script type="text/javascript">
var auto_refresh = setInterval(
function ()
{
$('#load_updates').load('index.php');
}, 500); // refresh every 10000 milliseconds

</script>
 </head>
 <body>
 
<div id="load_updates">
<?php
 	echo "El voltaje es: ";
	$myfile = fopen("log.txt", "r") or die("Unable to open file!");
	echo fread($myfile,filesize("log.txt"));
	echo " V";
	fclose($myfile);
?>
</div>
 </body>
</html>
