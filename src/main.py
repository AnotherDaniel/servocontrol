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



if __name__ == '__main__':
    import logging.config
    logging.basicConfig( level = logging.INFO )
    main()   
