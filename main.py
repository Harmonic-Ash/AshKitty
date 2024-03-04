from adafruit_servokit import ServoKit
import numpy as np
from Motion import *

vars = 0 # No of additional information required in arrays
servo_range = 180  #Servo range in degrees
position = np.zeros(16+vars)
print(position)


# pwm = ServoKit(channels=16)
for i in range(16):
    # # pwm.servo[i].set_pulse_width_range(1000,2000)  #Placeholder for setting pulsewidths
    # pwm.servo[i].actuation_range = servo_range
    # pwm.servo[i].angle = 90
    pass


def set_positions():

    pass

def level_compensation():
    pass
    # Need a Kalman filter for IMU data
    # Determine approximate yaw and pitch from the IMU
    # To level left/right, raise and lower each opposing side slightly.
    # To level front/back, raise and lower the front and back slightly.
    # Note gait may end up too short on these sides and it might turn left or right
    # Determine required compensation to keep level? Possible PI controller?

while True:
    command = input("Enter a command\n")
    if command == "start" or "Start":
        start()
    else:
        pass


# Need to loop through gaits.
# We need to know the current position, the next position and
# Do I create seperate functions for each gait, then call them to gait? Would be easier!
# Turn can use a control signal to determine how tight the turn is perhaps?
# Convert Petoi code into Python for gaits.
#

