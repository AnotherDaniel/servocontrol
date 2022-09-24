# servocontrol for a simple robot arm

Playground for fooling around with a self-made robot arm (e.g. [the EEZYbotARM Mk2](https://www.instructables.com/EEZYbotARM-Mk2-3D-Printed-Robot/))

Ground-breaking features include:

- development-mock of pigpio library
- convenient servo properties/interaction encapsulation
- separated-out servo properties definition
- mechanism for ramp-up and slow-down of servo actuation when driving to new position
- servo position range abstraction (can use raw setpoint or 0-100 position range)
- ability to define axis movement restriction dependencies ("this axis can only go to that point if that other axis is at least at that point")
- pre-defined robot arm positions

&nbsp;

---

## ToDos

- measure movement restriction ranges on real arm, test related code irl
- maybe add interactive arm control loop, where arm and target positions can be entered via keyboard?
