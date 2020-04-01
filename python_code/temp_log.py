#Imported libraries
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import os

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

#Call the blinkOnce function above in a loop when the touch sensor is pressed
def readF(temp_pin):
	humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
	temperature = temperature * 9/5.0 + 32

	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
		print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temperature, humidity))
	else:
		print('Something is broken, moron...')

	return tempFahr

try:
	with open("../log/temp_log.csv", "a") as log:
		while True:
			input_state = GPIO.input(button_pin)

			if input_state == True:
				for i in range (blink_time):
					blink_once(red_pin)
				time.sleep(.2)
				data1 = readF(temp_pin)
				data2 = readF(temp_pin)
				print('The Temperature is ' + data1)
				print('The Humidity is ' + data2)
				log.write("{0},{1}\n".format(time.strftime("%Y‐%m‐%d %H:%M:%S"),str(data1),str(data2)))
				log.flush()
				os.fsync(log)

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for blinking and thinking!')
	GPIO.cleanup()
