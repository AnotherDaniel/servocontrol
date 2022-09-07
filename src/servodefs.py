#!/usr/bin/python3

""" Configuration for servos/axis of our robot arm """
turn = { 'name': 'turn', 'pin': 17, 'min': 500, 'max': 1500, 'initial': 1000, 'startdelay': 75, 'mindelay_cw': 10, 'mindelay_ccw': 10 }
shoulder = { 'name': 'shoulder', 'pin': 18, 'min': 800, 'max': 1750, 'initial': 1200, 'startdelay': 75, 'mindelay_cw': 20, 'mindelay_ccw': 15 }
elbow = { 'name': 'elbow', 'pin': 19, 'min': 500, 'max': 1500, 'initial': 1200, 'startdelay': 75, 'mindelay_cw': 15, 'mindelay_ccw': 20 }
hand = { 'name': 'hand', 'pin': 20, 'min': 625, 'max': 1500, 'initial': 625, 'startdelay': 75, 'mindelay_cw': 10, 'mindelay_ccw': 10 }


""" Set of pre-defined standard positions """
pos_home = { 'turn': 50, 'shoulder': 50, 'elbow': 50, 'hand': 0 }
