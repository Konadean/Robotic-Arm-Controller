# Prototype code before seperated the controller obejct into its own class

#import evdev
from evdev import InputDevice, categorize, ecodes

import RPi.GPIO as GPIO
import pigpio
import time

#create 'gamepad' object
gamepad = InputDevice('/dev/input/event4')

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

rTrig = 9
lTrig = 10
rBump = 311
lBump = 310

lSt = 317
rSt = 318
select = 158
start = 315

lrDpad = 16
udDpad = 17

on_vals = [1, -1, 1023]

#     if event.value in on_vals:
class servo_move:
    
    def __init__(self):
        self.master = pigpio.pi()
        self.base = 500
        self.arm_1 = 1500
        self.arm_2 = 1500
        self.wrist = 1500
        self.left_claw = 1500
        self.right_claw = 1500
     

    def base_add(self):
        while True:
            event = gamepad.read_one()
            if self.base > 2500:
                break
            if event == None:
                self.base += 0.25
                self.master.set_servo_pulsewidth(18, self.base)
                #self.master.set_servo_pulsewidth(4, self.base)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def base_sub(self):
        while True:
            event = gamepad.read_one()
            if self.base <= 500:
                break
            if event == None:
                self.base -= 0.25
                self.master.set_servo_pulsewidth(18, self.base)
                #self.master.set_servo_pulsewidth(4, self.base)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def arm_1_add(self):
        while True:
            event = gamepad.read_one()
            if self.arm_1 > 2100:
                break
            if event == None:
                self.arm_1 += 0.125
                self.master.set_servo_pulsewidth(4, self.arm_1)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def arm_1_sub(self):
        while True:
            event = gamepad.read_one()
            if self.arm_1 <= 900:
                break
            if event == None:
                self.arm_1 -= 0.125
                self.master.set_servo_pulsewidth(4, self.arm_1)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
    
    def arm_2_add(self):
        while True:
            event = gamepad.read_one()
            if self.arm_2 > 2500:
                break
            if event == None:
                self.arm_2 += 0.125
                self.master.set_servo_pulsewidth(17, self.arm_2)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def arm_2_sub(self):
        while True:
            event = gamepad.read_one()
            if self.arm_2 <= 500:
                break
            if event == None:
                self.arm_2 -= 0.125
                self.master.set_servo_pulsewidth(17, self.arm_2)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def wrist_add(self):
        while True:
            event = gamepad.read_one()
            if self.wrist > 2500:
                break
            if event == None:
                self.wrist += 0.5
                self.master.set_servo_pulsewidth(27, self.wrist)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def wrist_sub(self):
        while True:
            event = gamepad.read_one()
            if self.wrist <= 500:
                break
            if event == None:
                self.wrist -= 0.5
                self.master.set_servo_pulsewidth(27, self.wrist)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
    
    def claw_open(self):
        while True:
            event = gamepad.read_one()
            if self.left_claw > 2500 or self.right_claw <= 500:
                break
            if event == None:
                self.left_claw += 1
                self.right_claw -= 1
                self.master.set_servo_pulsewidth(26, self.left_claw)
                self.master.set_servo_pulsewidth(16, self.right_claw)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def claw_close(self):
        while True:
            event = gamepad.read_one()
            if self.left_claw <= 1200 or self.right_claw > 1800:
                break
            if event == None:
                self.left_claw -= 1
                self.right_claw += 1
                self.master.set_servo_pulsewidth(26, self.left_claw)
                self.master.set_servo_pulsewidth(16, self.right_claw)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break



temp = servo_move()

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        if event.value in on_vals:
            if event.code == aBtn:
                print("A")
                temp.base_add()
            elif event.code == bBtn:
                print("B")
                temp.base_sub()
            elif event.code == xBtn:
                print("X")
                temp.arm_1_add()
            elif event.code == yBtn:
                print("Y")
                temp.arm_1_sub()
            elif event.code == rTrig:
                print("Right Trigger")
                
            elif event.code == lTrig:
                print("Left Trigger")
                
            elif event.code == rBump:
                print("Right Bumper")
                temp.wrist_add()
            elif event.code == lBump:
                print("Left Bumper")
                temp.wrist_sub()
            elif event.code == lSt:
                print("Left Stick")
                
            elif event.code == rSt:
                print("Right Stick")
                
            elif event.code == select:
                print("select")
                temp.claw_open()
            elif event.code == start:
                print("start")
                temp.claw_close()
            elif event.code == lrDpad:
                print("lrDpad")
                temp.arm_2_add()
            elif event.code == udDpad:
                print("udDpad")
                temp.arm_2_sub()

# Detecting for press
# while True:
#     event = gamepad.read_one()
#     if event == None:
#         pass
#     elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
#         # Detecting for unpress
#         base = 500
#         while True:
#             event = gamepad.read_one()
#             if base > 2500:
#                 break
#             if event == None:
#                 base += 0.5
#                 master.set_servo_pulsewidth(18, base)
#             elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
#                 break
#         break






        