import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

print("Starting up servo but making it hold for 2 sec")
servo1.start(0)
time.sleep(2)

print("rotating 180 in 10 80 degree steps")
duty = 2
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty += 1
    
time.sleep(2)

print("Turning back to 90 degrees for 2 sec")
servo1.ChangeDutyCycle(7)
time.sleep(2)

servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()
print("done")

