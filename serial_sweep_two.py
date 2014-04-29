"""Control two servos over serial.

This is for a servo with angles from 20-165.
"""

import glob
import platform
import serial
from time import sleep
import sys

def servo_iter():
	for pos in range(20,165):
		yield pos

if __name__ == "__main__":
	# find arduinos
	# note: currently this is Mac only
	arduinos = glob.glob('/dev/tty.usbmodem*')

	# select first arduino
	try:
		arduino = arduinos[0]
	except IndexError:
		print "No Arduinos found"
		sys.exit(1)


	print "Connecting to " + arduino

	try:
		# connect to serial port
		ser = serial.Serial(arduino, 115200)
	except:
		print "Failed to connect to Arduino"
		sys.exit(1)

	# need a short delay right after serial port is started for the Arduino to initialize
	sleep(2)

	# initialize generator
	pos = servo_iter()

	try:
		while True:
			try:
				x = pos.next()
			except StopIteration:
				pos = servo_iter()
				x = pos.next()
			print x
			
			# pad the servo value with zeros
			x = str(x).zfill(3)
			# for now we're sending the same value to both servos
			x = x + x

			# send data to the Arduino
			written = ser.write(x)

			# the minimum delay we can wait before sending another serial message
			sleep(1.1)
	# close the serial port on exit, or you will have to unplug the Arduino to connect again
	finally:
		ser.close()