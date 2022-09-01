#!/usr/bin/python3

# Configuration for servos/axis of our robot arm
turn = { 'name': 'turn', 'pin': 17, 'min': 500, 'max': 1500, 'initial': 1000 }
shoulder = { 'name': 'shoulder', 'pin': 18, 'min': 800, 'max': 1750, 'initial': 1000 }
elbow = { 'name': 'elbow', 'pin': 19, 'min': 500, 'max': 1500, 'initial': 800 }
hand = { 'name': 'hand', 'pin': 20, 'min': 625, 'max': 1500, 'initial': 625 }
