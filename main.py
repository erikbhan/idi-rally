#!/usr/bin/env pybricks-micropython
from Bot import Bot

robot = Bot()

robot.calibrate()
robot.wait_for_button()