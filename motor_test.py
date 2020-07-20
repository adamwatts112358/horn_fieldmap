#import Adafruit_BBIO.GPIO as GPIO
import config_parse
import time

'''
Test a single motor using the keyboard "s" and "d" keys for each direction.
'''

BB = config_parse.get_BB_params()

MotorX_dir = BB['MotorX_dir']
MotorX_step = BB['MotorX_step']
#GPIO.setup(MotorX_dir, GPIO.OUT)
#GPIO.setup(MotorX_step, GPIO.OUT)

MotorY_dir = BB['MotorY_dir']
MotorY_step = BB['MotorY_step']
#GPIO.setup(MotorY_dir, GPIO.OUT)
#GPIO.setup(MotorY_step, GPIO.OUT)

MotorZ_dir = BB['MotorZ_dir']
MotorZ_step = BB['MotorZ_step']
#GPIO.setup(MotorZ_dir, GPIO.OUT)
#GPIO.setup(MotorZ_step, GPIO.OUT)

print(MotorX_dir)
print(MotorX_step)
print(MotorY_dir)
print(MotorY_step)
print(MotorZ_dir)
print(MotorZ_step)

def move(dir_pin, step_pin):
#    GPIO.output(dir_pin, GPIO.HIGH)
#    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
#    GPIO.output(dir_pin, GPIO.LOW)
#    GPIO.output(step_pin, GPIO.LOW)

#def readPosition():

#print('Press: <s> = move left, <d> = move right, then <Enter>. Press CTRL+C to exit.')
#while 1:
#    variable = input()
#    if variable == 'b':
#        print("Moving forward")
#        #move(dir_pin, step_pin)
#        # Read position
#    elif variable == 'f':
#        print("Moving backward")
#        #move(dir_pin, step_pin)
#        # Read position
#    else:
#        print('Invalid command.')
#        print('Press: <s> = move left, <d> = move right, then <Enter>.')