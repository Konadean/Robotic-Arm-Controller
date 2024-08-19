import RPi.GPIO as GPIO
import pigpio
import time

#GPIO.setmode(GPIO.BOARD)

#MAX PULSE = 2500
#MIN PULE = 500
#270 Deg of Range --> Not Bad



# DAT.set_servo_pulsewidth(18, 2500)
# DAT.set_servo_pulsewidth(4, 2500)

#Base - 1600 Hz Centers

try:
    while True:
        master = pigpio.pi()
        choice = input("choose which sevo to change \n\n 1 - base \n\n 2 - arm seg 1\n\n3 - arm seg 2\n\n")
        if choice == '1':
            while True:
                # Min = 500
                # Mid = 1600
                # Max = 2500
                i = input("\n\nSpecify where to rotate the base to by between 500-2500.  Or type 'exit' to exit\n\n")
                if i == "exit":
                    break
                elif i == "min":
                    master.set_servo_pulsewidth(18, 500)
                elif i == "mid":
                    master.set_servo_pulsewidth(18, 1600)
                elif i == "max":
                    master.set_servo_pulsewidth(18, 2500)
                elif 500 <= int(i) and int(i) <= 2500:
                    master.set_servo_pulsewidth(18, int(i))   
        elif choice == '2':
            while True:
                i = input("\n\nSpecify where to rotate the arm to by between 900-2100.  Or type 'exit' to exit\n\n")
                if i == "exit":
                    break
                elif i == "min":
                    master.set_servo_pulsewidth(4, 900)
                elif i == "mid":
                    master.set_servo_pulsewidth(4, 1475)
                elif i == "max":
                    master.set_servo_pulsewidth(4, 2100)
                elif 850 <= int(i) and int(i) <= 2150:
                    master.set_servo_pulsewidth(4, int(i))
        elif choice == '3':
            while True:
                i = input("\n\nSpecify where to rotate the arm to by between 500-2500.  Or type 'exit' to exit\n\n")
                if i == "exit":
                    break
                elif i == "min":
                    master.set_servo_pulsewidth(17, 500)
                elif i == "mid":
                    master.set_servo_pulsewidth(17, 1600)
                elif i == "max":
                    master.set_servo_pulsewidth(17, 2500)
                elif 500 <= int(i) and int(i) <= 2500:
                    master.set_servo_pulsewidth(17, int(i))
        else:
            print("\n\ninvalid choice.  Choose again")
except ValueError:
    print("\n\ninvalid choice.")
finally:
    print("\n\ngoodbye")
