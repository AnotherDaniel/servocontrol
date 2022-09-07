#!/usr/bin/python3
import servocontrol as sc
import threading
import logging
logger = logging.getLogger(__name__)

class armcontrol:
    """ Abstraction for an entire robot arm, handling all axis' servos and providing some convenience functions, 
        e.g. for https://www.instructables.com/EEZYbotARM-Mk2-3D-Printed-Robot/ """
    
    # list of servocontrol references
    servocontrols = []

    def __init__( self, servos = [] ):
        """ Add servo configs as list of servodef-style servo dictionaries """
        logging.debug( "[armcontrol] call to __init__()" )
        if len( servos ) > 0:
            for servo in servos:
                self.add_servo( servo )

    def __del__( self ):
        logging.debug( "[armcontrol] call to __del__()" )
        for sc in self.servocontrols:
            for servo in sc:
                sc[servo].release()

    def add_servo( self, servo ):
        """ Add one servo as servodef-style servo dictionary """
        logging.debug( "[armcontrol] call to add_servo()" )
        self.servocontrols.append( { servo['name']: sc.servocontrol( **servo ) } )

    def drive_to( self, servo_name, target ):
        """ Drive servo_name axis to position target (movement range value between 0-100) """
        logging.debug( "[armcontrol] call to drive_to()" )
        for sc in self.servocontrols:
            if servo_name in sc:
                sc[servo_name].drive_to( target )
                return

    def drive_to_t( self, servo_name, target ):
        """ Drive servo_name axis to position target (movement range value between 0-100) - threaded """
        logging.debug( "[armcontrol] call to drive_to_t()" )
        t = threading.Thread(target=self.drive_to, args=(servo_name, target, ))
        t.start()
        return t

    def drive_to_pos( self, position = {} ):
        """ Drive robot arm to position, individual axis targets provided by servodef-style position dictionary """
        logging.debug( "[armcontrol] call to drive_to_pos()" )
        for key, pos in position.items():
            for sc in self.servocontrols:
                if key in sc:
                    self.drive_to( key, pos )

    def drive_to_pos_t( self, position = {} ):
        """ Drive robot arm to position, individual axis targets provided by servodef-style position dictionary - threaded """
        logging.debug( "[armcontrol] call to drive_to_pos_t()" )
        threads = []
        for key, pos in position.items():
            for sc in self.servocontrols:
                if key in sc:
                    threads.append( self.drive_to_t( key, pos ) )

        for t in threads:
            t.join()

    def report_pos( self ):
        """ Print current robot arm axis positions to logger.info (movement range value between 0-100) """
        logging.debug( "[armcontrol] call to report_pos()" )
        for sc in self.servocontrols:
            for servo in sc:
                logging.info( "" + servo + ":" + str( sc[servo].get_position() ) )
