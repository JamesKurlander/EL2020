#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
import time
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import picamera

PIR_pin = 4
touch_pin = 12
eFROM = "james.h.kurlander@gmail.com"
eTO = "james.h.kurlander@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(touch_pin, GPIO.IN)

#runs indefinitely, checking the area for any movement
def detect():
	for i in range(101):
		if GPIO.input(PIR_pin):
			print("Entity detected!")
			from subprocess import call
			call(["aplay", "/home/james/EL2020/final/audio_files/we_got_em.wav"])
			capture()
			time.sleep(1000)
		elif GPIO.input(touch_pin):
			print("SYSTEM DISARMED")
			exit()
		else:
			print("Nothing detected...")
		time.sleep(1)

#captures an image of the intruder when called
def capture():
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		camera.start_preview()
		time.sleep(2)
		camera.capture('intruder.jpg')
		alert('intruder.jpg')

#takes in an image and alerts the owner through an email with an image of the intruder
def alert(img_file):
	img_data = open(img_file, 'rb').read()
	msg = MIMEMultipart()
	msg['Subject'] = 'INTRUDER ALERT!'
	msg['From'] = eFROM
	msg['To'] = eTO

	text = MIMEText("Here's a photo of the perpetrator! Go check it out! Here's a livestream of the action: http://192.168.1.204:2020/")
	msg.attach(text)
	image = MIMEImage(img_data, name=os.path.basename(img_file))
	msg.attach(image)

	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(eFROM, "twxqclibkkepzisu")
	server.sendmail(eFROM, eTO, msg.as_string())
	server.quit()

detect()
GPIO.cleanup()
