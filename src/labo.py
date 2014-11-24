#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys,os
import serial
import socket

dir = "./log.txt"
port = '/dev/ttyACM0'
ser = serial.Serial(port,9600)

def getTime():
	return time.strftime("%Y;%m;%d;%H;%M;%S")

def is_valid_number(number):
	"""In this case numbers higher than 100 will be considered
	serial communication errors"""
	if float(number) > 100:
		#print "Error while validating %s ." % number
		return False
	else:
		return True

def is_valid(data):
	try:
		float(data)
		#Passes first test	
		aux = data.split('.')
		if (len(aux[1]) is 2):
			#Passes second test
			return is_valid_number(data) 
	except:
		#print "Error while validating %s ." % data
		return False

while True:
	try:
		hora = getTime()
		f = open(dir,"a")
		p = open('/var/www/log.txt',"w+")
		volt = ser.readline()
		volt = volt.replace('\r\n','')
		if is_valid(volt):
			pass
		else:
			continue			
		print volt
		s=hora+";"+volt+'\n';
		f.write(s);
		p.write(volt);
	except KeyboardInterrupt:
		print "Exited cleanly"
		break
	
	#except :
		#break

