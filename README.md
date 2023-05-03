# EEL4660C-Robotics-Project
A class project that involved an autonomous robot that uses an Arduino and a Raspberry Pi.

The project used the following items:
- 1 x Ultrasonic sensor
- 1 x Parallax Robotics Kit (includes 2 Servo Motors)
- 1 x Arduino Uno Rev 3
- 1 x Raspberry Pi model 3B
- 1 x Pi Camera

It uses a modified forward based approach to detect items through the Ultrasonic sensor, however, is not saved in the system, so it detects it on a base by base cases depending on the conditions met.
When an object is detected, it moves back for a few seconds and scans its sourroundings to determine the best course of action.
