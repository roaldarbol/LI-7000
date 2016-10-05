import datetime
import serial
import time

def li7000_readline(port):
	#port.flush()
	output = port.readline()
	return output

def li7000_write(port, str):
	port.write(bytes(str.encode()))

def li7000_header(port):
	port.flushInput()
	port.flushOutput()
	time.sleep(0.1)
	port.write(bytes("(RS232(Sources?))\n".encode()))
	output = li7000_readline(port)
	return output
	
def li7000_pollnow(port):
	port.flushInput()
	port.flushOutput()
	time.sleep(0.1)
	port.write(bytes("(RS232(Poll Now))\n".encode()))
	for i in range (0, 3):
		if i == 2:
			output = li7000_readline(port)
			print(output)
		else:
			li7000_readline(port)

f1 = open("LI-7000.txt", "a")
#f2 = open("time.txt", "a")
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout = 1)

while 1:
	choice = raw_input("header or data? \n")
	#print(choice)
	if choice == "header":
		print(li7000_header(ser))

	elif choice == "data":
		li7000_pollnow(ser)
	else:
		continue
