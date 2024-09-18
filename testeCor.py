#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
botao = TouchSensor(Port.S1)
sensorCor = ColorSensor(Port.S2)

def testeCor():
    ref = sensorCor.reflection()
    cor = sensorCor.color()
    print('Cor: ', cor)
    print('Ref: ', ref)


    while True:
        novaCor = sensorCor.color()
        novaRef = sensorCor.reflection()
        if cor != novaCor or ref != novaRef:
            print("\x1b[2J\x1b[H")  # Limpar a tela do console
            print('Cor: ', novaCor)
            print('Ref: ', novaRef)
            cor = novaCor
            ref = novaRef