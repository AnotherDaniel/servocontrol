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

- This looks not too bad at this point; stuff isn't working reliably but I think that is not due to the code at this point, more these stupid servos.
- What are these last niggs about? Do stuff with cgroups on piopigd?
