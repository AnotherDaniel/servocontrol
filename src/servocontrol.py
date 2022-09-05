#!/usr/bin/python3
# Helper module that encapsulates servo properties and pigpiod interaction for manipulating a robot arm
# (e.g. https://www.instructables.com/EEZYbotARM-Mk2-3D-Printed-Robot/)

#import pigpio as pigpio
import mockpig as pigpio
import time
import logging
logger = logging.getLogger(__name__)

# Absolute min - max limits for what we allow in actuation
MIN = 500
MAX = 2500
STARTDELAY = 275
MINDELAY = 50

pwm = pigpio.pi()

class servocontrol:
    name = None
    pin = None
    min = None
    max = None
    startdelay = STARTDELAY
    mindelay = MINDELAY
    position = None
 
    def __init__( self, name, pin, min, max, initial, startdelay=STARTDELAY, mindelay=MINDELAY ):
        assert pin >= 2 and pin <= 27
        assert max > min

        self.name = name
        self.pin = pin
        self.min = min
        self.max = max
        self.position = initial
        self.startdelay = startdelay
        self.mindelay = mindelay

        global pwm
        pwm.set_mode( self.pin, pigpio.OUTPUT )
        pwm.set_PWM_frequency( self.pin, 50 )
        self.drive_to_raw( self.position )

    def __del__( self ):
        global pwm
        pwm.set_PWM_dutycycle( self.pin, 0 )
        pwm.set_PWM_frequency( self.pin, 0 )

    def get_name( self ):
        assert self.name is not None
        return self.name

    def get_position_raw( self ):
        # Returns current position as raw pwm value as dealt with by pigpio library
        assert self.position is not None
        return self.position

    def get_position( self ):
        # Returns current position as value between 0 - 100 
        assert self.position is not None
        range = self.max - self.min
        step = range/100
        pos = self.position - self.min
        return int(pos/step)
 
    def drive_to_raw( self, target ):
        # 'target' parameter is raw pwm value as expected by pigpio library
        # Idea for this function is to have a ramped speed-up and slow-down for servo actuation
        global pwm
        global MIN
        global MAX
        assert self.position >= MIN and self.position <= MAX
        assert target >= self.min and target <= self.max

        logging.debug( "[servocontrol] call to drive_to( " + str(self.name) + ", " + str(target) + " )" )

        delta = 0
        delay = self.startdelay
        decel = self.startdelay - self.mindelay

        # This is to address both right-turn and left-turn cases with one loop (below)
        if target > self.position:
            delta = 1
        elif target < self.position:
            delta = -1
        else:
            return

        while (delta > 0 and self.position < target) or (delta < 0 and self.position > target):
#            if (delta > 0 and self.position >= target) or (delta < 0 and self.position <= target):
#                break

            self.position += delta
            pwm.set_servo_pulsewidth( self.pin, self.position );
            time.sleep( delay/200000 )

            # abs(target-position) > decel  is to compute slowdown-point regardless of turn direction
            if delay > self.mindelay and abs(target-self.position) > decel:
                delay -= 1
            elif delay < self.startdelay and abs(target-self.position) < decel:
                delay += 1

    def drive_to( self, target ):
        # 'target' parameter is a position value between 0 - 100
        assert target >= 0 and target <= 100
        range = self.max - self.min
        step = range/100
        delta = step*target
        self.drive_to_raw( self.min + delta )
