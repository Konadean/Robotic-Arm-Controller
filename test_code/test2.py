import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50)

pwm.start(0)
time.sleep(1)

c = 2
while c <= 6:
    pwm.ChangeDutyCycle(10*c)
    time.sleep(0.25)
    c = c + 2


pwm.stop()
GPIO.cleanup()
print("done")
