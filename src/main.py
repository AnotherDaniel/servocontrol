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
    arm.add_restriction( sd.elbow_shoulder1 )
    arm.add_restriction( sd.elbow_shoulder2 )

    arm.report_pos()

    # drive to pre-defined position
    print( "arm to home" )
    arm.drive_to_pos( sd.pos_home )
    arm.report_pos()
    #input( "Hit enter to continue" )
    time.sleep( 1 )

    # axis = "turn"

    # # drive one specific servo/axis
    # print( axis+" to 0" )
    # arm.drive_to( axis, 0 )
    # arm.report_pos()
    # input( "Hit enter to continue" )

    # # drive one specific servo/axis
    # print( axis+" to 100" )
    # arm.drive_to( axis, 100 )
    # arm.report_pos()
    # input( "Hit enter to continue" )

    # # drive one specific servo/axis
    # print( axis+" to 50" )
    # arm.drive_to( axis, 50 )
    # arm.report_pos()
    # input( "Hit enter to continue" )

    # drive to manually defined target position
    print( "arm to 0es" )
    arm.drive_to_pos( { 'turn': 0, 'shoulder': 0, 'elbow': 10, 'hand': 0 } )
    arm.report_pos()
    input( "Hit enter to continue" )
#    time.sleep( 1 )

    # drive to manually defined target position
    print( "arm to 100s" )
    arm.drive_to_pos( { 'turn': 100, 'shoulder': 80, 'elbow': 100, 'hand': 100 } )
    arm.report_pos()
    input( "Hit enter to continue" )
#    time.sleep( 1 )

    # drive to manually defined target position
    print( "arm to somewhere else" )
    arm.drive_to_pos( { 'turn': 33, 'shoulder': 75, 'elbow': 17, 'hand': 5 } )
    arm.report_pos()
    input( "Hit enter to continue" )
#    time.sleep( 1 )

    # drive to pre-defined position
    print( "arm to home" )
    arm.drive_to_pos( sd.pos_home )
    arm.report_pos()

    del arm


if __name__ == '__main__':
    import logging.config
    logging.basicConfig( level = logging.INFO )
    main()   
