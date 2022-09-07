#!/usr/bin/python3

import pigpio as pigpio
#import mockpig as pigpio
import threading
import time
import logging
logger = logging.getLogger(__name__)

# Absolute min - max limits for what we allow in actuation
MIN = 500
MAX = 2500

# Timing-related definions - STARTDELAY and MINDELAY influence movment start/end and max-speeds, 
# ALACRITY is a value that influences how these speeds are interpreted (higher value = faster movement )
STARTDELAY = 275
MINDELAY = 50
ALACRITY = 20000

pwm = pigpio.pi()

class servocontrol:
    """ Encapsulate servo properties and pigpiod interaction for controlling RC-style servos """
    name = None
    pin = None
    min = MIN
    max = MAX
    startdelay = STARTDELAY
    mindelay_cw = MINDELAY
    mindelay_ccw = MINDELAY
    position = None

    lock = threading.Lock()
 
    def __init__( self, name, pin, min, max, initial, startdelay=STARTDELAY, mindelay_cw=MINDELAY, mindelay_ccw=MINDELAY ):
        """ Create servo abstraction, providing the following properties:
            - name: name or servo/axis
            - pin: Raspberry GPIO pin that servo is controlled by
            - min: minimum pigpio-style PWM threshold (500 is a good start value if you don't know better)
            - max: maximum pigpio-style PWM threshold (1500 is a good start value if you don't know better)
            - initial: initial servo position for initialization
            - startdelay: start speed for servo actuation
            - mindelay_cw: max speed during servo actuation for clock-wise turns 
            - mindelay_ccw: max speed during servo actuation for counter-clock-wise turns
        """
        # Sanity check - Raspberry Pi only has GPIO pins between 2 - 27 
        assert pin >= 2 and pin <= 27
        assert max > min
        assert MIN <= initial and initial <= MAX
        assert mindelay_cw < startdelay and mindelay_ccw < startdelay

        self.name = name
        self.pin = pin
        self.min = min
        self.max = max
        self.position = initial
        self.startdelay = startdelay
        self.mindelay_cw = mindelay_cw
        self.mindelay_ccw = mindelay_ccw

        logging.debug( "[servocontrol] call to __init__()" )

        global pwm
        pwm.set_mode( self.pin, pigpio.OUTPUT )
        pwm.set_PWM_frequency( self.pin, 50 )
        self.drive_to_raw( self.position )

    def __del__( self ):
        logging.debug( "[servocontrol] call to __del__()" )
        pass

    def release( self ):
        global pwm
        assert pwm is not None
        logging.debug( "[servocontrol] call to release()" )
        pwm.set_PWM_dutycycle( self.pin, 0 )
        pwm.set_PWM_frequency( self.pin, 0 )

    def get_name( self ):
        """ Name of servo/axis """
        assert self.name is not None
        logging.debug( "[servocontrol] call to get_name()" )
        return self.name

    def get_position_raw( self ):
        """ Current position as raw PWM value as dealt with by pigpio library """
        assert self.position is not None
        logging.debug( "[servocontrol] call to get_position_raw()" )
        return self.position

    def get_position( self ):
        """ Returns current position as value between 0 - 100 """
        assert self.position is not None
        logging.debug( "[servocontrol] call to get_position()" )
        range = self.max - self.min
        step = range/100
        pos = self.position - self.min
        return int(pos/step)
 
    def drive_to_raw( self, target ):
        """ Argument 'target' is raw pwm value as expected by pigpio library """

        # Motivation for this function is to have a ramped speed-up and slow-down for servo actuation
        global pwm
        global MIN
        global MAX
        assert pwm is not None
        assert self.position >= MIN and self.position <= MAX
        assert target >= self.min and target <= self.max

        logging.debug( "[servocontrol] call to drive_to_raw( " + str(self.name) + ", " + str(target) + " )" )

        decel = None
        mindelay = None
        delta = 0

        # This is to address both right-turn and left-turn cases with one loop (below)
        if target > self.position:
            delta = 1
            mindelay = self.mindelay_cw
        elif target < self.position:
            delta = -1
            mindelay = self.mindelay_ccw
        else:
            return

        # delay is the current-loop-iteration delay between PWM actuations,
        delay = self.startdelay

        with self.lock:
            while (delta > 0 and self.position < target) or (delta < 0 and self.position > target):
                self.position += delta
                pwm.set_servo_pulsewidth( self.pin, self.position )
                time.sleep( delay/ALACRITY )

                # decel is the number of loops (increments/decrements) needed to get from start/end-delay to minimum delay
                decel = self.startdelay - max( delay, mindelay )

                # abs(target-position) is the delta (number of loop iterations remaining) to target position
                if delay > mindelay and abs(target-self.position) > decel:
                    delay -= 1
                elif delay < self.startdelay and abs(target-self.position) < decel:
                    delay += 1

                #print( "<position> " + str(self.position) + "  -  <delay> " +str( delay ) )

    def drive_to( self, target ):
        """ Argument 'target' is a position value between 0 - 100 """
        assert target >= 0 and target <= 100
        logging.debug( "[servocontrol] call to drive_to( " + str(self.name) + ", " + str(target) + " )" )
        range = self.max - self.min
        step = range/100
        delta = step*target
        self.drive_to_raw( self.min + delta )
