# #import evdev
# from evdev import InputDevice, categorize, ecodes
# 
# #create 'gamepad' object
# gamepad = InputDevice('/dev/input/event4')
# 
# print(gamepad)
# 
# for event in gamepad.read_loop():
#     print(categorize(event))

# #import evdev
# from evdev import InputDevice, categorize, ecodes
# 
# #create 'gamepad' object
# gamepad = InputDevice('/dev/input/event4')
# 
# print(gamepad)
# 
# for event in gamepad.read_loop():
#     if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
#         print(categorize(event))

#import evdev
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

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        if event.value in on_vals:
            if event.code == aBtn:
                print("A")
            elif event.code == bBtn:
                print("B")
            elif event.code == xBtn:
                print("X")
            elif event.code == yBtn:
                print("Y")
            elif event.code == rTrig:
                print("Right Trigger")
            elif event.code == lTrig:
                print("Left Trigger")
            elif event.code == rBump:
                print("Right Bumper")
            elif event.code == lBump:
                print("Left Bumper")
            elif event.code == lSt:
                print("Left Stick")
            elif event.code == rSt:
                print("Right Stick")
            elif event.code == select:
                print("select")
            elif event.code == start:
                print("start")
            elif event.code == lrDpad:
                print("lrDpad")
            elif event.code == udDpad:
                print("udDpad")






























