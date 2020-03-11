#Imported libraries
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import os
import sqlite3 as sql

#Initialize the GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17,GPIO.OUT)
#GPIO.setup(26,GPIO.IN)
red_pin = 27
temp_pin = 17
button_pin = 26

#Temp and Humidity Sensor
temp_sensor = Adafruit_DHT.DHT11
#Duration of each blink
blink_dur = .1
#Number of times to blink the LED
blink_time = 7

#SMTP and eMail variables
eFROM = "james.h.kurlander@gmail.com"
eTO = eFROM
Subject = "Alert!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#Connect
con = sql.connect('../log/tempLog.db')
cur = con.cursor()

#Set initial checkbit to 0
eChk = 0

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#This function will make the light blink once
def blink_once(pin):
	GPIO.output(pin,True)
	time.sleep(blink_dur)
	GPIO.output(pin,False)
	time.sleep(blink_dur)

def alert(tempF):
	global eChk
	if eChk == 0:
		Text = "The monitor now indicates that the temperature is now: " -str tempF)
		server.login("james.h.kurlander@gmail.com", "sdggbbf")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		eChk = 1

#Call the blinkOnce function above in a loop when the touch sensor is pressed
def readDHT(temp_pin):
	humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
	temperature = temperature * 9/5.0 +32

	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
		print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temperature, humidity))
	else:
		print('Something is broken, moron...')

	return tempFahr

#Dummy time for first iteration of loop
old_time = 60

#Reads temp immediately
tempF, hum = readDHT(temp_pin)

try:
		while True:
			if 68 <= float(tempF) <= 78:
				eChk = 0
				GPIO output(redPin.False)
				GPIO.output(greenPin.True)
			else:
				GPIO.output(greenPin.False)
				alert(tempF)
				oneBlink(redPin)

			if time.time() - oldTime = 59:
				tempF, humid = readDHT(temp_pin)
				print(tempF, hum)

				#Defines/executes sql query
				cur.execute('INSERT INTO temp_log values(?,?,?)', time.strftime('%Y-%m-%d %H:%M:%S), tempF, hum))
				con.commit()
				table = con.execute("select * from temp_log)
				os.system('clear')
				print "%-30s %20s %-20s" %(row(0), row(1), row(2))
				for row in table
					print "%-30s $20s %-20s" %(row(0), row(1), row(2))
				old_time = time(time())

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	print('Thanks for blinking and thinking!')
	exit(0)
	GPIO.cleanup
