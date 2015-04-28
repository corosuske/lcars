import time
import os
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18
#door_pin = 23
led_pin = 4
io.setup(pir_pin, io.IN)         # activate input
#io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

io.setup(led_pin, io.OUT) 
loopcount = 0
io.output(led_pin, False)

#while True:
#    if io.input(pir_pin):
#        print("PIR ALARM!")
#	io.output(led_pin, True)
#	os.system("date > /home/pi/motion.log")
#	loopcount = 0  
#    else: 
#	loopcount = loopcount + 1 
#        io.output(led_pin, False)
#    #if io.input(door_pin):
#    #    print("DOOR ALARM!")
#    time.sleep(0.5)
#    if loopcount == 30:
#	print("30 sec of slence")
