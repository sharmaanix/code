import RPi.GPIO as GPIO
from time import sleep
import sys ,tty ,termios

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03,GPIO.OUT)
pwm=GPIO.PWM(03,50)
pwm.start(0)
print 'se4tup up has been done'

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
	
angle=0	

while(True):
	print"enter the arrow:',' to increase by 10 degree and '.' to decrease by 10 degree"
	t=getch()
	
	if t=='.':
		if angle in range(0,181):
			angle=angle+10
			setangle(angle)
			
		else:
			print'the angle is out of range'	
	elif t==',':
		if angle in range(0,181):
			angle=angle-10
			setangle(angle)
		else:
			print'the angle is out of range'
	
			
		
			
		
	
	

