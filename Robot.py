from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

class Robot():
    def __init__(self):
        self.brobot = DriveBase(left_motor=Motor(Port.B), right_motor=Motor(Port.C), wheel_diameter=55, axle_track=127)
        self.left_color_sensor, self.right_color_sensor = ColorSensor(Port.S4), ColorSensor(Port.S2)
        self.ev3 = EV3Brick()
        self.RED, self.GREEN, self.BLUE = 50, 50, 50

    def print_to_screen(self, text):
        char[] ch = new char[text.length]
        

    def calibrate(self):
        self.ev3.screen.print("COLOR CALIBRATION:\nL-SENSOR: WHITE\nR-SENSOR: BLACK\nPUSH A BUTTON\nTO CONTINUE")
        self.wait_for_button()
        self.ev3.screen.clear()

        RED_ON_WHITE, GREEN_ON_WHITE, BLUE_ON_WHITE = self.left_color_sensor.rgb()
        RED_ON_BLACK, GREEN_ON_BLACK, BLUE_ON_BLACK = self.right_color_sensor.rgb()

        self.RED = (RED_ON_WHITE + RED_ON_BLACK) // 2
        self.GREEN = (GREEN_ON_WHITE + GREEN_ON_BLACK) // 2
        self.BLUE = (BLUE_ON_WHITE + BLUE_ON_BLACK) // 2

    def wait_for_button(self):
        while True:
            if self.ev3.buttons.pressed():
                break
            continue

    def is_black(self, color_sensor):
        (red, green, blue) = color_sensor.rgb()
        if red < self.RED and green < self.GREEN and blue < self.BLUE:
            return True
        else:
            return False