#!/usr/bin/python3
import logging
import RPi.GPIO as GPIO
import pigpio
import time

MIN = 500
MAX = 2500
turn = 17
shoulder = 18
elbow = 19
hand = 20
position = 500  # initialize to 0 degrees



def driveto(pwm, target):
    global position
    assert position >= MIN and position <= MAX
    assert target >= MIN and target <= MAX

    logging.debug("   position: "+str(position)+"   target: "+str(target))

    delta = 0
    startdelay = 275
    mindelay = 50
    delay = startdelay
    decel = startdelay-mindelay

    # This is to address both right-turn and left-turn cases with one loop (below)
    if target > position:
        delta = 1
    elif target < position:
        delta = -1
    else:
        return

    while position != target:
        position += delta
        pwm.set_servo_pulsewidth( servo, position );
        time.sleep( delay/200000 )

        # abs(target-position) > decel  is to compute slowdown-point regardless of turn direction
        if delay > mindelay and abs(target-position) > decel:
            delay -= 1
        elif delay < startdelay and abs(target-position) < decel:
            delay += 1


servo = turn

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth
logging.basicConfig( level = logging.INFO )
pwm = pigpio.pi()
pwm.set_mode( servo, pigpio.OUTPUT )
pwm.set_PWM_frequency( servo, 50 )


pwm.set_servo_pulsewidth( servo, 1000 );


driveto(pwm, 1000)

#driveto(pwm, 800)

#driveto(pwm, 900)


# hand min:  625
# hand max: 1500

# elbow min: 625
# elbow max: 1600

# shoulder min: 800
# shoulder max: 1750

# turn min:
# turn mid: 800
# turn max:

# turning off servo
pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_frequency( servo, 0 )
