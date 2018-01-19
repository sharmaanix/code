import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03,GPIO.OUT)
pwm=GPIO.PWM(03,50)
pwm.start(0)
print 'setup up has been done'


def setangle (angle):
	
	duty =(angle/18)+2
	GPIO.output(03,True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	pwm.ChangeDutyCycle(0)
	print'angle set: %d'%angle
while(True):
		l =raw_input("enter the arrow:'<' means 0 degree and '>' means 180 degree")
		print'you have  entered is %s and the motor will work accordinglgy'%l
		if l=='<':
			angle=0	
			setangle(angle)
			sleep(3)
		elif l=='>':
			angle=180
			setangle(angle)
			sleep(3)
		else:
			print'the input you have entered is out of scope'
			


