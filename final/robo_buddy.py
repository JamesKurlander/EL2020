import RPi.GPIO as GPIO
import time
import os
import time
import smtplib
import socket

PIR_pin = 4
eFROM = "james.h.kurlander@gmail.com"
eTO = "james.h.kurlander@gmail.com"
Subject = "Intruder Alert!"
Text = "An intruder has been spotted! Go check it out!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_pin, GPIO.IN)

def detect():
	for i in range(101):
		if GPIO.input(PIR_pin):
			print("Entity detected!")
			alert()
		else:
			print("Nothing detected...")
		time.sleep(2)

def alert():
	eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
	server.login(eFROM, "twxqclibkkepzisu")
	server.sendmail(eFROM, eTO, eMessage)
	server.quit

detect()
GPIO.cleanup()
