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

 - intermittently, motions are spasmically fast, or just wrong; soft real-time control capabilities (lack of) of the Raspi?