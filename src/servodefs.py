#!/usr/bin/python3

""" Configuration for servos/axis of our robot arm """
turn = { 'name': 'turn', 'pin': 17, 'min': 500, 'max': 1500, 'initial': 1000, 'startdelay': 275, 'mindelay_cw': 50, 'mindelay_ccw': 50 }
shoulder = { 'name': 'shoulder', 'pin': 18, 'min': 800, 'max': 1750, 'initial': 1000, 'startdelay': 275, 'mindelay_cw': 50, 'mindelay_ccw': 50 }
elbow = { 'name': 'elbow', 'pin': 19, 'min': 500, 'max': 1500, 'initial': 800, 'startdelay': 275, 'mindelay_cw': 50, 'mindelay_ccw': 75 }
hand = { 'name': 'hand', 'pin': 20, 'min': 625, 'max': 1500, 'initial': 625, 'startdelay': 275, 'mindelay_cw': 50, 'mindelay_ccw': 50 }


""" Set of pre-defined standard positions """
pos_home = { 'turn': 50, 'shoulder': 50, 'elbow': 50, 'hand': 0 }