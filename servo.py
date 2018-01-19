import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03,GPIO.OUT)
pwm=GPIO.PWM(03,50)
pwm.start(0)
print 'se4tup up has been done'

def setangle (angle):
	
	duty =(angle/18)+2
	GPIO.output(03,True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	pwm.ChangeDutyCycle(0)
	print'angle set: %d'%angle

	
while(True):
	setangle(0)
	sleep(2)
	setangle(180)
	sleep(2)  
pwm.stop()
GPIO.cleanup()	
print'program ended'



