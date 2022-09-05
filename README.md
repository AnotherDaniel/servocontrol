# servocontrol for a simple robot arm

Playground for fooling around with a self-made robot arm (e.g. https://www.instructables.com/EEZYbotARM-Mk2-3D-Printed-Robot/)

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

- make ramp-up/-down timings configurable (per servo) - and might we need different ramps/speeds per direction (where gravity plays a role in up/down movements)?
- add threading to armcontrol, so that multiple servos can be actuated in parallel
