import sys ,tty ,termios
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03,GPIO.OUT)
pwm=GPIO.PWM(03,50)
pwm.start(0)

print'setup up has been done'
angle=0
print'setting angle to : %d'%angle
def getch():
	
	fd=sys.stdin.fileno()
	old_settings=termios.tcgetattr(fd)
	
	try:
		tty.setraw(sys.stdin.fileno())
		ch=sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
	return ch
	
	
def setangle (angle):
	
	duty =(angle/18)+2
	GPIO.output(03,True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	pwm.ChangeDutyCycle(0)
	print'angle set: %d'%angle
 
 
while(True):
	print"press ',' to decrease  the angle by 30 degree or press '.' to increase the angle by 30 degree" 
	
	t=getch()
	if t=='.':
		if angle in range(0,180):
			angle=angle+30
			setangle(angle)
		else:
			print'the angle is exceeding the range'
			angle=0
	if t==',':	
		if angle in range(30,180):
			angle=angle-30
			setangle(angle)
		else:
			print'the angle is exceeding the range'
			angle=0	
	
	else:
		print' the key you pressed doesnot symbolize the value we expect'
				
pwm.stop()
GPIO.cleanup()	
print'program ended'

	
			 				 	
