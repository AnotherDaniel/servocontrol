#!/usr/bin/python3
import servocontrol as sc
import servodefs as sd
import logging

turn = None
shoulder = None
elbow = None
hand = None

def drive_to_pos( turn_target, shoulder_target, elbow_target, hand_target ):
    global turn
    global shoulder
    global elbow
    global hand
    turn.drive_to( turn_target )
    shoulder.drive_to( shoulder_target )
    elbow.drive_to( elbow_target )
    hand.drive_to( hand_target )

def report_pos():
    global turn
    global shoulder
    global elbow
    global hand
    logging.info("turn:" + str(turn.get_position()) +
                " - shoulder:" + str(shoulder.get_position()) +
                " - elbow:" + str(elbow.get_position()) +
                " - hand:" + str(hand.get_position()) )

def main():
    global turn
    global shoulder
    global elbow
    global hand
    
    # initialization
    turn = sc.servocontrol( **sd.turn )
    shoulder = sc.servocontrol( **sd.shoulder )
    elbow = sc.servocontrol( **sd.elbow )
    hand = sc.servocontrol( **sd.hand )

    # do stuff here
    turn.drive_to( 44 )
    report_pos()

    drive_to_pos( **sd.pos_home )
    report_pos()

    # cleanup
    del turn
    del shoulder
    del elbow
    del hand

if __name__ == '__main__':
    import logging.config
    logging.basicConfig( level = logging.INFO )
    main()   
