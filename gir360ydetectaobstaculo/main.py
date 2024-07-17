#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.parameters import Port

ev3 = EV3Brick()
obstacle_sensor = UltrasonicSensor(Port.S4)

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)


robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


ev3.speaker.beep()


while True:
    
    robot.turn(360)

    while obstacle_sensor.distance() > 300:
        wait(10)
        
        ev3.light.off()
        wait(1000)
    ev3.light.on(Color.RED)
    wait(500)
    ev3.light.off()
    
    
  
