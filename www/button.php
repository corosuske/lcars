<?php

#controll led nr1 
if ($_GET['led_on']) {
  # This code will run if ?run=true is set.
  exec("sudo python /home/pi/ledon.py");
  }
elseif ($_GET['led_off']) {
  exec("sudo python /home/pi/ledoff.py");
  }

#controll led2
elseif ($_GET['led_on2']) {
  # This code will run if ?run=true is set.
  exec("sudo python /home/pi/ledon2.py");
  }
elseif ($_GET['led_off2']) {
  exec("sudo python /home/pi/ledoff2.py");
  }

#controll both leds 
elseif ($_GET['all_led_on']) {
  # This code will run if ?run=true is set.
  exec("sudo python /home/pi/ledon2.py & sudo python /home/pi/ledon.py");
  }
elseif ($_GET['all_led_off']) {
  exec("sudo python /home/pi/ledoff2.py & sudo python /home/pi/ledoff.py");
  }


?>

<body bgcolor="#000000">
<p>
<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
<a href="?led_on=true"><img border="0" alt="on" src="img/on.png" width="201" height="76""></a>

#<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
#<a href="?led_off=true"><img border="0" alt="off" src="img/off.png" width="201" height="76"></a>
</p>
<p>
<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
<a href="?led_on2=true"><img border="0" alt="on" src="img/on.png" width="201" height="76"></a>

#<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
#<a href="?led_off2=true"><img border="0" alt="off" src="img/off.png" width="201" height="76"></a>
</p>
<p>
<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
<a href="?all_led_on=true"><img border="0" alt="on" src="img/on.png" width="201" height="76"></a>

#<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
#<a href="?all_led_off=true"><img border="0" alt="off" src="img/off.png" width="201" height="76"></a>
</p>
</body>
?>
