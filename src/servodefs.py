#!/usr/bin/python3

""" Configuration for servos/axis of our robot arm 
    - name: name or servo/axis
    - pin: Raspberry GPIO pin that servo is controlled by
    - min: minimum pigpio-style PWM threshold (500 is a good start value if you don't know better)
    - max: maximum pigpio-style PWM threshold (1500 is a good start value if you don't know better)
    - initial: initial servo position for initialization
    - startdelay: start speed for servo actuation
    - mindelay_cw: max speed during servo actuation for clock-wise turns 
    - mindelay_ccw: max speed during servo actuation for counter-clock-wise turns
"""
turn = { 'name': 'turn', 'pin': 17, 'min': 500, 'max': 2500, 'initial': 1500, 'startdelay': 75, 'mindelay_cw': 10, 'mindelay_ccw': 10 }
shoulder = { 'name': 'shoulder', 'pin': 18, 'min': 800, 'max': 1400, 'initial': 800, 'startdelay': 125, 'mindelay_cw': 40, 'mindelay_ccw': 25 }
elbow = { 'name': 'elbow', 'pin': 19, 'min': 500, 'max': 1500, 'initial': 500, 'startdelay': 110, 'mindelay_cw': 25, 'mindelay_ccw': 40 }
hand = { 'name': 'hand', 'pin': 20, 'min': 625, 'max': 1500, 'initial': 625, 'startdelay': 75, 'mindelay_cw': 15, 'mindelay_ccw': 15 }

""" If there exist movement-range dependencies between different axes, that can be modelled as follows:
        axisX_axisY = { 'axisX': ['<', 30, 'axisY', '<', 20 ] }
    This is interpreted as "axisY can only go lesser than 30 if axisY is lesser than 20".
    Setpoints within the restricted areas are interpolated linearly, i.e. the above example would allow axisX moving to 15 if axisY is at or below 10.
    Allowed syntax: valid axis names as per arm configuration, '<' or '>' for movement range restriction boundaries (< means "0 to value", > means "value to 100").
"""
elbow_shoulder1 = { 'elbow': ['<', 30, 'shoulder', '<', 20 ] }
elbow_shoulder2 = { 'elbow': ['>', 80, 'shoulder', '>', 70 ] }

""" Set of pre-defined standard positions """
# home position - aligned with the initial-points of the main servos (above), useful as shutdown position to avoid big spams on init 
pos_home = { 'turn': 50, 'shoulder': 10, 'elbow': 0, 'hand': 0 }
