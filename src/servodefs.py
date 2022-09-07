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
turn = { 'name': 'turn', 'pin': 17, 'min': 500, 'max': 1500, 'initial': 1000, 'startdelay': 75, 'mindelay_cw': 10, 'mindelay_ccw': 10 }
shoulder = { 'name': 'shoulder', 'pin': 18, 'min': 800, 'max': 1400, 'initial': 1200, 'startdelay': 125, 'mindelay_cw': 30, 'mindelay_ccw': 15 }
elbow = { 'name': 'elbow', 'pin': 19, 'min': 500, 'max': 1500, 'initial': 1200, 'startdelay': 100, 'mindelay_cw': 15, 'mindelay_ccw': 50 }
hand = { 'name': 'hand', 'pin': 20, 'min': 625, 'max': 1500, 'initial': 625, 'startdelay': 75, 'mindelay_cw': 10, 'mindelay_ccw': 10 }


""" Set of pre-defined standard positions """
pos_home = { 'turn': 50, 'shoulder': 10, 'elbow': 10, 'hand': 0 }
