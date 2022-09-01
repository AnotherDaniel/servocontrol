#!/usr/bin/python3
import servocontrol as sc
import servodefs
import logging


def main():
    turn = sc.servocontrol( **servodefs.turn )
    shoulder = sc.servocontrol( **servodefs.shoulder )
    elbow = sc.servocontrol( **servodefs.elbow )
    hand = sc.servocontrol( **servodefs.hand )

    # do stuff here
    logging.info( "current turn pos: " + str(turn.get_position_raw()) )
    turn.drive_to_raw( 1234 )
    logging.info( "new turn pos: " + str(turn.get_position_raw()) )

    turn.drive_to( 0 )
    logging.info( "new turn pos: " + str(turn.get_position()) )

    turn.drive_to( 50 )
    logging.info( "new turn pos: " + str(turn.get_position()) )

    turn.drive_to( 100 )
    logging.info( "new turn pos: " + str(turn.get_position()) )

    del turn
    del shoulder
    del elbow
    del hand


if __name__ == '__main__':
    import logging.config
    logging.basicConfig( level = logging.INFO )
    main()   
