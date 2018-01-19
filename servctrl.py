import socket
import sys
from _thread import *
import sys ,tty ,termios
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03,GPIO.OUT)
pwm=GPIO.PWM(03,50)
pwm.start(0)
angle=0
host=''
port=5550
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
try:
	 s.bind((host,port))
	 
except socket.error as e:
	print(str(e))

s.listen(5)

print'waiting for connection'

def setangle (angle):
	
	duty =(angle/18)+2
	GPIO.output(03,True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	pwm.ChangeDutyCycle(0)
	
def exceedingangle():
	print'the angle is exceeding the range'
	angle=0
	reply='the angle is exceeding the range'
	return angle
		
	
def threaded_client(conn):
	conn.send(str.encode("Type the angle  to which you want to rotate in range from 0 to 180"))
	while True:
		data=conn.recv(2048)
		print'data received %s '%data
		l=data
		
		if l==".":
			if angle in range(0,180):
				angle=angle+30
				setangle(angle)
				reply='servo angle is set to %d angle'%angle
			else:
				exceedingangle()
				
		elif l==",":	
			if angle in range(30,180):
				angle=angle-30
				setangle(angle)
				reply='servo angle is set to %d angle'%angle
			else:
				exceedingangle()	
	
		else:
			print' the key you pressed doesnot symbolize the value we expect'
			reply=' the key you pressed doesnot symbolize the value we expect'
		
		
				
		if not data :
			break
		conn.send(str.encode(str(reply)))
		
			
	conn.close()
	
while True:
	conn,addr=s.accept()
	print('connected to:',addr[0],':',str(addr[1]))
	start_new_thread(threaded_client,(conn,))			 


pwm.stop()
GPIO.cleanup()
