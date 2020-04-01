#Imports the Rpi.GPIO library and renames it to GPIO
#This it simply done to make things easier when calling the library
import RPi.GPIO as GPIO
#Imports the Adafruit_DHT library and renames it to DHT
import Adafruit_DHT as DHT

temp_pin = 17
temp_sensor = DHT.DHT11

while True:
	hum, temp = DHT.read_retry(temp_sensor, temp_pin)
	temp = temp * 9/5.0 + 32

	if hum is not None and temp is not None:
		print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temp, hum))
	else:
		print('Something is broken, moron...')
