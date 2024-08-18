from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import pigpio

class ServoMove:

    def __init__(self, gamepad):
        self.master = pigpio.pi()
        self.base = 500
        self.rear_arm = 1500
        self.fore_arm = 1500
        self.wrist = 1500
        self.left_claw = 1500
        self.right_claw = 1500
        self.gamepad = gamepad
     

    def base_cw(self):
        while True:
            event = self.gamepad.read_one()
            if self.base > 2500:
                break
            if event == None:
                self.base += 0.25
                self.master.set_servo_pulsewidth(18, self.base)
                #self.master.set_servo_pulsewidth(4, self.base)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def base_ccw(self):
        while True:
            event = self.gamepad.read_one()
            if self.base <= 500:
                break
            if event == None:
                self.base -= 0.25
                self.master.set_servo_pulsewidth(18, self.base)
                #self.master.set_servo_pulsewidth(4, self.base)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def rear_arm_cw(self):
        while True:
            event = self.gamepad.read_one()
            if self.rear_arm > 2100:
                break
            if event == None:
                self.rear_arm += 0.125
                self.master.set_servo_pulsewidth(4, self.rear_arm)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def rear_arm_ccw(self):
        while True:
            event = self.gamepad.read_one()
            if self.rear_arm <= 900:
                break
            if event == None:
                self.rear_arm -= 0.125
                self.master.set_servo_pulsewidth(4, self.rear_arm)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
    
    def fore_arm_cw(self):
        while True:
            event = self.gamepad.read_one()
            if self.fore_arm > 2500:
                break
            if event == None:
                self.fore_arm += 0.125
                self.master.set_servo_pulsewidth(17, self.fore_arm)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def fore_arm_ccw(self):
        while True:
            event = self.gamepad.read_one()
            if self.fore_arm <= 500:
                break
            if event == None:
                self.fore_arm -= 0.125
                self.master.set_servo_pulsewidth(17, self.fore_arm)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def wrist_cw(self):
        while True:
            event = self.gamepad.read_one()
            if self.wrist > 2500:
                break
            if event == None:
                self.wrist += 0.5
                self.master.set_servo_pulsewidth(27, self.wrist)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
            
    def wrist_ccw(self):
        while True:
            event = self.gamepad.read_one()
            if self.wrist <= 500:
                break
            if event == None:
                self.wrist -= 0.5
                self.master.set_servo_pulsewidth(27, self.wrist)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break
    
    def claw_open(self):
        while True:
            event = self.gamepad.read_one()
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
            event = self.gamepad.read_one()
            if self.left_claw <= 1200 or self.right_claw > 1800:
                break
            if event == None:
                self.left_claw -= 1
                self.right_claw += 1
                self.master.set_servo_pulsewidth(26, self.left_claw)
                self.master.set_servo_pulsewidth(16, self.right_claw)
            elif event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                break