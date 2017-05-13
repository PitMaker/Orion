#gestion du gyroscope

#imports
import smbus
import time
import os
import math
import RPi.GPIO as GPIO


#création d'une class gyroscope
class Gyroscope(object):
	"""Création d'un gyroscope branché à SCL et SDA"""
	bus = smbus.SMBus(1)
	def __init__(self):
		# Réglage de de la définition. Le 3e parametre est 0x05 pour mesurer de -2g a +2g, 0x09 de -4g a +4g, 0x01 de -8g a +8g
        self.bus.write_byte_data(0x1D, 0x16, 0x05) 
		#variables calibration
		self.cal_x , self.cal_y, self.cal_z 
		#variables des coordonnées calibrées
		self.x, self.y, self.z
		#calibration qui donne x, y, z à 0
		self.calibration()

	def calibration(self):
		#séquence pour mise à zéro des coordonnées du rêpère
		x = self.bus.read_byte_data(0x1D, 0x06)
		y = self.bus.read_byte_data(0x1D, 0x07)
		z = self.bus.read_byte_data(0x1D, 0x08)
		self.cal_x = (-x)
		self.cal_y = (-y)
		self.cal_z = (-z + 63)

	def getValueX(self):
        return self.bus.read_byte_data(0x1D, 0x06) + self.cal_x
    def getValueY(self):
        return self.bus.read_byte_data(0x1D, 0x07) + self.cal_y
    def getValueZ(self):
        return self.bus.read_byte_data(0x1D, 0x08) + self.cal_z


######## PROGRAMME TEST ##########
gyro = Gyroscope()

# on répète la mesure 1000 fois avant de s'arrêter 
for a in range(1000):
    x = gyro.getValueX()
    if (x > 127):         # les valeurs se trouvent entre 0 et 255, 
        x = x - 255       # alors qu'on les veut entre -127 et 127
    y = gyro.getValueY()
    if (y > 127):
        y = y - 255 
    z = gyro.getValueZ()
    if (z > 127):
        z = z - 255 

    # valeur totale de l'accélération, peu importe l'orientation
    total = math.sqrt(x*x+y*y+z*z); 

    # calcul des angles et conversion en degrés
    angleX = round(math.asin(x/ total )*180.0/3.1416)
    angleY = round(math.asin(y/ total )*180.0/3.1416)
    angleZ = round(math.acos(z/ total )*180.0/3.1416)

    total = round (total)
   
    print 'x = {0}  y = {1}  z = {2}  total = {3}  anglex = {4}°  angley = {5}°  anglez = {6}°'.format(x,y,z,total,angleX,angleY,angleZ)
    # (ligne précédente à modifier un peu si vous êtes en python 3)

    time.sleep(0.5)    # pour que l'écriture à l'écran ne soit pas exagérément rapide.
