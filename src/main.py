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

    ## drive to manually defined target position
    print( "arm to somewhere" )
    arm.drive_to_pos( { 'turn': 50, 'shoulder': 5, 'elbow': 25, 'hand': 0 } )
    arm.report_pos()
#    input( "Hit enter to continue" )
    time.sleep( 1 )


#     ## drive to manually defined target position
#     print( "arm to somewhere else" )
#     arm.drive_to_pos( { 'turn': 50, 'shoulder': 80, 'elbow': 50, 'hand': 0 } )
#     arm.report_pos()
# #    input( "Hit enter to continue" )
#     time.sleep( 1 )

#     ## drive to manually defined target position
#     print( "arm to somewhere else again" )
#     arm.drive_to_pos( { 'turn': 50, 'shoulder': 5, 'elbow': 75, 'hand': 0 } )
#     arm.report_pos()
# #    input( "Hit enter to continue" )
#     time.sleep( 1 )

    # drive to pre-defined position
    print( "arm to home" )
    arm.drive_to_pos( sd.pos_home )
    arm.report_pos()

    del arm


if __name__ == '__main__':
    import logging.config
    logging.basicConfig( level = logging.WARN )
    main()   
