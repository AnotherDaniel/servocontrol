#!/usr/bin/python3

import servocontrol as sc
import time
import logging
logger = logging.getLogger(__name__)

class armcontrol:
    # list of servocontrol references
    servocontrols = []

    def __init__( self, servos = [] ):
        # add servo configs as list of servodef-style dicts
        
        if len( servos ) > 0:
            for servo in servos:
                self.add_servo( servo )

    def __del__( self ):
        for servo in self.servocontrols:
            del servo

    def add_servo( self, servo ):
        self.servocontrols.append( { servo['name']: sc.servocontrol( **servo ) } )

    def drive_to( self, servo_name, target ):
        for sc in self.servocontrols:
            if servo_name in sc:
                sc[servo_name].drive_to( target )
                pass

    def drive_to_pos( self, position = {} ):
        for key, pos in position.items():
            for sc in self.servocontrols:
                if key in sc:
                    sc[key].drive_to( pos )

    def report_pos( self ):
        for sc in self.servocontrols:
            for servo in sc:
                logging.info( "" + servo + ":" + str( sc[servo].get_position() ) )
