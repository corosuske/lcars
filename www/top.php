
<html>
<head>
<title>(Type a title for your page here)</title>
<script type="text/javascript"> 
function display_c(){
var refresh=1000; // Refresh rate in milli seconds
mytime=setTimeout('display_ct()',refresh)
}

function display_ct() {
var strcount
var x = new Date()
document.getElementById('ct').innerHTML = x;
tt=display_c();
}
</script>
</head>
#<body bgcolor="#000000">
<b>
<center>
<img border="0" alt="on" src="img/topline.png" width="250" height="15"">
<font face="verdana" size="3" color="#ff9900">
<body bgcolor="#000000" onload=display_ct();>
<span id='ct' ></span>
</center>
</b>
</font>
</body>
</html>


