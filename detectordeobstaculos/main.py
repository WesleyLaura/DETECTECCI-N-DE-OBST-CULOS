#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
obstacle_sensor = UltrasonicSensor(Port.S4)

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)


robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


ev3.speaker.beep()


while True:
    
    robot.drive(200, 0)

    while obstacle_sensor.distance() > 150:
        wait(10)

    robot.straight(-150)


    robot.turn(90)