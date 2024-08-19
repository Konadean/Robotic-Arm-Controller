from gpiozero import Servo
from time import sleep


def back_forth():
	servo = Servo(25)
	val = -1
	increment = 0.1
	try:
		while True:
			servo.value = val
			sleep(0.1)
			val += increment
			if val > 1:
				increment *= -1
	except KeyboardInterrupt:
		print("Program stopped")

back_forth()