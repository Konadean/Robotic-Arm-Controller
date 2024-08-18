import ServoMove
import time
from evdev import InputDevice, categorize, ecodes

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

temp = ServoMove(gamepad)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        if event.value in on_vals:
            if event.code == aBtn:
                print("A")
                temp.base_cw()
            elif event.code == bBtn:
                print("B")
                temp.base_ccw()
            elif event.code == xBtn:
                print("X")
                temp.rear_arm_cw()
            elif event.code == yBtn:
                print("Y")
                temp.rear_arm_ccw()
            elif event.code == rTrig:
                print("Right Trigger")
                
            elif event.code == lTrig:
                print("Left Trigger")
                
            elif event.code == rBump:
                print("Right Bumper")
                temp.wrist_cw()
            elif event.code == lBump:
                print("Left Bumper")
                temp.wrist_ccw()
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
                temp.fore_arm_cw()
            elif event.code == udDpad:
                print("udDpad")
                temp.fore_arm_ccw()

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






        