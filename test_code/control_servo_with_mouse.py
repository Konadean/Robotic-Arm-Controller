import RPi.GPIO as GPIO  
import time

from pynput.mouse import Listener

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
s1 = GPIO.PWM(12, 50)

s1.start(0)


#angle = 0

def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    angle = 0
    if button == button.left and pressed:
        angle += 1
        s1.ChangeDutyCycle(2+angle/28)
#         s1.ChangeDutyCycle(2+90/28)
        time.sleep(0.5)
        s1.ChangeDutyCycle(0)
    elif button == button.right and pressed:
        angle -= 1
        s1.ChangeDutyCycle(2+angle/28)
#         s1.ChangeDutyCycle(2+180/28)
        time.sleep(0.5)
        s1.ChangeDutyCycle(0)        

def on_scroll(x, y, dx, dy):
    angle = 0
    s1.ChangeDutyCycle(2+angle/28)
    time.sleep(0.5)
    s1.ChangeDutyCycle(0)   
    s1.stop()
    GPIO.cleanup()
    print("Hee Hee")

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

        

    