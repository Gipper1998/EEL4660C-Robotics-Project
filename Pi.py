import RPi.GPIO as GPIO
import serial
import time
import picamera

GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 21
GPIO_ECHO = 20

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def main():
	print("Running. Press CTRL-C to exit.")
	with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
		time.sleep(0.1) #wait for serial to open
		if arduino.isOpen():
			print("{} connected!".format(arduino.port))
			try:
				while True:
					dist = distance()
					print("Measured Distance = %.1f cm" % dist)
					if dist < 20.0:
						take_photo()
						distM = distance()
						arduino.write(b'0')
						time.sleep(0.5)
						arduino.write(b'2')
						time.sleep(0.75)
						arduino.write(b'0')
						time.sleep(0.5)
						arduino.write(b'3')
						time.sleep(0.5)
						arduino.write(b'0')
						distL = distance()
						time.sleep(0.5)
						arduino.write(b'4')
						time.sleep(1)
						arduino.write(b'0')
						distR = distance()
						time.sleep(1)
						if (distR > distL and distM):
							arduino.write(b'0')
						elif (distM > distR > distL):
							arduino.write(b'3')
							time.sleep(0.5)
							arduino.write(b'0')							
						else:
							arduino.write(b'3')
							time.sleep(1)
							arduino.write(b'0')
					else:
						arduino.write(b'1')
					time.sleep(0.1) # wait for arduino to answer
					arduino.flushInput() #remove data after reading
			except KeyboardInterrupt:
				print("KeyboardInterrupt has been caught.")
				GPIO.cleanup()

def take_photo():
	#Take picture if object is close
	camera = picamera.PiCamera()
	camera.rotation = 180
	camera.capture('/home/pi/Desktop/img.jpg')
	camera.close()
	
def distance():
	#set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)
	
	#set Tigger after 0.01 ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	
	StartTime = time.time()
	StopTime = time.time()
	
	#save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
		
	#save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
	
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2
	
	return distance

if __name__ == "__main__":
	main()
