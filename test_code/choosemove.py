import RPi.GPIO as GPIO  
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
s1 = GPIO.PWM(12, 50)

s1.start(0)

try:
    while True:
        angle = float(input("Enter angle between 0 & 180: "))
        if angle < 0:
            angle = -1*angle
        s1.ChangeDutyCycle(5+angle/72)
        time.sleep(0.5)
        s1.ChangeDutyCycle(0)
finally:
    s1.stop()
    GPIO.cleanup()
    print("L8tr bitch")
    
