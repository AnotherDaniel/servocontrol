#!/usr/bin/python3
# Drop-in mock for pigpio library - for development purposes

import logging
logger = logging.getLogger(__name__)

OUTPUT = 1

class pi:
    def set_mode( self, servo, mode ): 
        logging.debug("[mockpig] call to set_mode(" + str(servo) + ", " + str(mode) + ")")

    def set_PWM_frequency( self, servo, freq ):
        logging.debug("[mockpig] call to set_PWM_frequency(" + str(servo) + ", " + str(freq) + ")")

    def set_PWM_dutycycle( self, servo, cycle ):
        logging.debug("[mockpig] call to set_PWM_dutycycle(" + str(servo) + ", " + str(cycle) + ")")

    def set_servo_pulsewidth( self, servo, pulsewidth ):
        logging.debug("[mockpig] call to set_servo_pulsewidth(" + str(servo) + ", " + str(pulsewidth) + ")")
        