#!/usr/bin/env pybricks-micropython
from Robot import Robot

robot = Robot()

robot.calibrate()
robot.ev3.screen.print("READY: PUSH A BUTTON\nREADY: PUSH A BUTTON\nREADY: PUSH A BUTTON\nREADY: PUSH A BUTTON")
robot.wait_for_button()
robot.ev3.screen.clear()
