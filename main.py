#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from testeCor import testeCor
from frases import frasesIA
import os


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
botao = TouchSensor(Port.S1)
sensorCor = ColorSensor(Port.S2)



# Write your program here.



while True:
    ev3.speaker.beep()

    contadorOlhos = 1
    ev3.screen.load_image(ImageFile.TIRED_RIGHT)
    while botao.pressed() == False:
        if contadorOlhos == 80:
            img = ImageFile.TIRED_RIGHT
            ev3.screen.load_image(img)
        elif contadorOlhos == 15:
            img = ImageFile.TIRED_LEFT
            ev3.screen.load_image(img)
        elif contadorOlhos == 100:
            contadorOlhos = 0

        contadorOlhos += 1

        wait(50)

        
    contagem = 0
    ev3.screen.load_image(ImageFile.DIZZY)
    while sensorCor.color() == None and sensorCor.reflection() < 2:   #substituir true pelo valor de parada 
        
        if contagem < len(frasesIA):
            contagem +=1
        else:
            contagem = 0
        
            
        wait(40)
        


    ev3.screen.load_image(ImageFile.UP)
    
    print("\x1b[2J\x1b[H")  # Limpar a tela do console
    ev3.speaker.beep(100, 150)
    print('.')
    wait(1000)
    ev3.speaker.beep(100, 150)
    print('.')
    wait(1000)
    ev3.speaker.beep(100, 150)
    print('.')
    wait(1000)
    

    ev3.speaker.beep(600, 200)
    print("\x1b[94m" + frasesIA[contagem])  # Imprimir em cor azul
    print("\x1b[0m")  # Restaurar cor padrão
    
        
    