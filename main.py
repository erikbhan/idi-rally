#!/usr/bin/env pybricks-micropython
from Robot import Robot

robot = Robot()

robot.calibrate()

robot.wait_for_button()