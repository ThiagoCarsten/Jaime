#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
motor_direita = Motor(Port.B)
motor_esquerda = Motor(Port.C)
jaime = DriveBase(motor_esquerda, motor_direita, wheel_diameter=43.2, axle_track=104)
cor_direita = ColorSensor(Port.S3)
cor_esquerda = ColorSensor(Port.S2)

velocidade_normal = 100
velocidade_curva = 30

while cor_esquerda.color() != Color.RED and cor_direita.color() != Color.RED:

    if cor_esquerda.color() == Color.WHITE and cor_direita.color() == Color.WHITE:
        jaime.drive(velocidade_normal, 0)
        ev3.screen.print("BRANCO E/D")

    elif cor_esquerda.color() == Color.BLACK and cor_direita.color() == Color.WHITE:
        jaime.drive(velocidade_curva, -200)
        ev3.screen.print("PRETO E")

    elif cor_esquerda.color() == Color.WHITE and cor_direita.color() == Color.BLACK: 
        jaime.drive(velocidade_curva, 200)
        ev3.screen.print("PRETO D")
