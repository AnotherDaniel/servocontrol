# servocontrol for a simple robot arm

Playground for fooling around with a self-made robot arm (e.g. [the EEZYbotARM Mk2](https://www.instructables.com/EEZYbotARM-Mk2-3D-Printed-Robot/))

Ground-breaking features include:

- development-mock of pigpio library
- convenient servo properties/interaction encapsulation
- separated-out servo properties definition
- mechanism for ramp-up and slow-down of servo actuation when driving to new position
- servo position range abstraction (can use raw setpoint or 0-100 position range)
- pre-defined robot arm positions

&nbsp;

---

## ToDos

- make initial positioning (on construction) also use ramp up/down actuation
- look into pigpio exception on cleanup

Exception ignored in: <function servocontrol.__del__ at 0xffff9faa9900>
Traceback (most recent call last):
  File "/home/ubuntu/workspace/servocontrol/src/servocontrol.py", line 70, in __del__
  File "/usr/local/lib/python3.10/dist-packages/pigpio.py", line 1480, in set_PWM_dutycycle
  File "/usr/local/lib/python3.10/dist-packages/pigpio.py", line 1025, in _pigpio_command
AttributeError: 'NoneType' object has no attribute 'send'
