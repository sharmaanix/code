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
	
	
	
def threaded_client(conn):
	conn.send(str.encode("Type the angle  to which you want to rotate in range from 0 to 180"))
	while True:
		data=conn.recv(2048)
		angle=int(data)
		print'data received %d degree '%angle
		setangle(angle)
		reply='servo angle is set to (in degrees):'+data.decode('utf-8')
				
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
