#!/usr/bin/python3
import servocontrol as sc
import threading
import logging
from util import log_info
logger = logging.getLogger(__name__)

class armcontrol:
    """ Abstraction for an entire robot arm, handling all axis' servos and providing some convenience functions, 
        e.g. for https://www.instructables.com/EEZYbotARM-Mk2-3D-Printed-Robot/ """
    
    # list of servocontrol references and dynamic range restrictions
    servocontrols = []
    restrictions = []

    def __init__( self, servos = None, restrictions = None ):
        """ Add servo configs as list of servodef-style servo dictionaries and movement restrictions """
        logging.debug( "[armcontrol] call to __init__()" )

        if servos is None:
            servos = []

        if len( servos ) > 0:
            for servo in servos:
                self.add_servo( servo )

        if restrictions is not None:
            self.restrictions = restrictions

    def __del__( self ):
        logging.debug( "[armcontrol] call to __del__()" )
        for sc in self.servocontrols:
            for servo in sc:
                sc[servo].release()

    def add_servo( self, servo ):
        """ Add one servo as servodef-style servo dictionary """
        logging.debug( "[armcontrol] call to add_servo()" )
        self.servocontrols.append( { servo['name']: sc.servocontrol( **servo ) } )

    def add_restriction( self, restriction ):
        """ Add servodef-style movement restriction """
        logging.debug( "[armcontrol] call to add_restriction()" )
        self.restrictions.append( restriction )

    @log_info
    def calc_restriction( self, target, restriction ):
        """ Calculate movement restriction based on input target and restriction """
        logging.debug( "[armcontrol] call to calc_restriction()" )

        left_dep = restriction[0]
        left_thresh = restriction[1]
        right_axis = restriction[2]
        right_dep = restriction[3]
        right_thresh = restriction[4]

        if eval( str(target)+" "+left_dep+" "+str(left_thresh) ):
            # (we have a restriction on target axis and) depending axis target is within restricted range
            
            right_pos = None
            for sc in self.servocontrols:
                if right_axis in sc:
                    right_pos = sc[right_axis].get_position()
                    break
            if right_pos is None:
                return target

            if eval( str(right_pos)+" "+right_dep+" "+str(right_thresh) ):
                # dependent axis position is within restriction-range
                # get rel pos of right_axis in right restricted space
                # compute rel pos of left axis based on that
                left_rel = None
                right_rel = None
                left_range = left_thresh
                # this is to record whether we're moving towards 0 or 100 (for final target calc)
                target_offset = 0

                # compute rel pos in restricted range for depending axis, percentage-to-outer-limit (0 or 100)
                if left_dep == '<':
                    left_rel = 1 - target/left_thresh
                elif left_dep == '>':
                    left_rel = (target-left_thresh) / (100-left_thresh)
                    left_range = 100 - left_thresh
                    target_offset = left_thresh
                else:
                    return target
                
                # compute rel pos in restricted range for dependent axis, percentage-to-outer-limit (0 or 100)
                if right_dep == '<':
                    right_rel = 1 - right_pos/right_thresh
                elif right_dep == '>':
                    right_rel = (right_pos-right_thresh) / (100-right_thresh)
                else:
                    return target
        
                assert left_rel is not None and right_rel is not None

                if left_rel > right_rel:
                    # apply the relative amount of movement from right axis to target axis/range, offset in case we're moving towards 100
                    torig = target
                    target = target_offset + int( right_rel * left_range )
                    logging.info( "original target: %i -> new target: %i (dep axis res-area position: %1.2f)"%(torig, target, right_rel) )

        return target

    def drive_to( self, servo_name, target ):
        """ Drive servo_name axis to position target (movement range value between 0-100) """
        logging.debug( "[armcontrol] call to drive_to()" )

        # check whether there are any applicable movement-restriction dependencies
        for res in self.restrictions:
            if servo_name in res:
                logger.info("Driving "+servo_name+" to "+str(target))
                target = self.calc_restriction( target, res[servo_name] )

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

    def drive_to_pos( self, position = None ):
        """ Drive robot arm to position, individual axis targets provided by servodef-style position dictionary """
        if position is None:
            return

        logging.debug( "[armcontrol] call to drive_to_pos()" )
        for key, pos in position.items():
            for sc in self.servocontrols:
                if key in sc:
                    self.drive_to( key, pos )

    def drive_to_pos_t( self, position = None ):
        """ Drive robot arm to position, individual axis targets provided by servodef-style position dictionary - threaded """
        if position is None:
            return

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
