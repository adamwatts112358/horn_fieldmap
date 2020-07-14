import Adafruit_BBIO.GPIO as GPIO

# Add a repeater loop so could make 10 moves with single function call, etc.

# X-axis
def move_left(X_dir_pin, X_step_pin):
    # Implement step multiplier
    GPIO.output(dir_pin, GPIO.HIGH)
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
def move_right(X_dir_pin, X_step_pin):
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)

# Y-axis
def move_up(Y_dir_pin, Y_step_pin):
    GPIO.output(dir_pin, GPIO.HIGH)
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
def move_down(Y_dir_pin, Y_step_pin):
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)

# Z-axis    
def move_forward(Z_dir_pin, Z_step_pin):
    GPIO.output(dir_pin, GPIO.HIGH)
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
def move_back(Z_dir_pin, Z_step_pin):
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
        