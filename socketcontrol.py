import socket
import sys
from _thread import *

 
host=''
port=5558
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
try:
	 s.bind((host,port))
	 
except socket.error as e:
	print(str(e))

s.listen(5)

print'waiting for connection'

def threaded_client(conn):
	conn.send(str.encode("press ',' to decrease  the angle by 30 degree or press '.' to increase the angle by 30 degree"))
	while True:
		data=conn.recv(2048)
		reply='server output:'+data.decode('utf-8')
		
		if not data:
			break
		conn.send(str.encode(str(reply)))
	conn.close()
	
while True:
	conn,addr=s.accept()
	print('connected to:',addr[0],':',str(addr[1]))
	start_new_thread(threaded_client,(conn,))			 
