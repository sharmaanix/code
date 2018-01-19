import sys ,tty ,termios

def getch():
	print'inside the getch loop'
	fd=sys.stdin.fileno()
	old_settings=termios.tcgetattr(fd)
	
	try:
		tty.setraw(sys.stdin.fileno())
		ch=sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
	return ch
	
t=getch()
print'the value for the keyboard input is: %s'%t

			
