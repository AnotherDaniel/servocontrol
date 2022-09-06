#!/usr/bin/python3
import servocontrol as sc
import servodefs as sd
import armcontrol as ac
import time
import logging

arm = None

def main():
    global arm
    arm = ac.armcontrol( [ sd.turn, sd.shoulder, sd.elbow, sd.hand ] )
    
    arm.report_pos()

    arm.drive_to( "elbow", 5 )
    arm.report_pos()

    arm.drive_to_pos_t( { 'turn': 78, 'shoulder': 2, 'elbow':85, 'hand': 67 } )
    arm.report_pos()

    arm.drive_to_pos_t( sd.pos_home )
    arm.report_pos()

if __name__ == '__main__':
    import logging.config
    logging.basicConfig( level = logging.DEBUG )
    main()   
