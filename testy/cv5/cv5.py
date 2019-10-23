# -*- coding: utf-8 -*-

"""
1. Create virtual environemnt:
mkdir pool
python -m venv pool
cd pool
Scripts\activate.bat

2. Install pip and Qt:
python -m pip install --upgrade pip
pip install PyQt5

3. Run example
cd ..
python cv5.py
cd pool
Scripts\deactivate.bat
"""

import math
import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

#http://www.riverbankcomputing.co.uk/software/pyqt/download
#self.map = QtGui.QPixmap(self.img.transformed(QtGui.QTransform(self.flip, 0, 0, 0, 1, 0, 0, 0, 1)))

class Fish(object):
  def __init__(self, file_name, living_area):
    self.img = QtGui.QImage(file_name)
    self.map = QtGui.QPixmap(self.img)
    self.img_rect = QtCore.QRectF(0, 0, self.img.width(), self.img.height())
    self.flip = 0
    self.size = random.uniform(200, 300)
    self.aspect = self.img.height() / float(self.img.width())
    self.living_area = living_area
    
    self.x = random.uniform(self.half_width(), living_area.playground.width() - self.half_width())
    self.y = random.uniform(self.half_height(), living_area.playground.height() - self.half_height())

    self.velocity = random.uniform(5, 20)
    self.azimuth = random.uniform(0, 360)
    
  def half_width(self):
    return self.size * 0.5
    
  def half_height(self):
    return self.size * self.aspect * 0.5
    
  def move(self, dt = 1):
    self.x += self.velocity * math.cos(self.azimuth) * dt
    self.y += self.velocity * math.sin(self.azimuth) * dt

    if((self.x <= self.half_width()) or self.x >= self.living_area.playground.width() - self.half_width()
    or self.y <= self.half_height()) or self.y >= self.living_area.playground.height() - self.half_height():
      self.velocity = random.uniform(1, 10)
      self.azimuth += random.uniform(0, 180)

  def draw(self, painter):
    rectangle = QtCore.QRectF(QtCore.QPointF(self.x - self.half_width(), self.y - self.half_height()), QtCore.QSizeF(self.size, self.size*self.aspect))
    painter.drawPixmap(rectangle, self.map, self.img_rect)

class Aquarium(QtWidgets.QMainWindow):
  def __init__(self):
    super(Aquarium, self).__init__()
    self.initUI()
        
  def initUI(self):
    self.setWindowTitle("Aquarium")
    
    self.playground = QtGui.QPixmap()
    self.playground.load("aquarium_1024.jpg")
    self.playground_rect = QtCore.QRectF(0, 0, self.playground.width(), self.playground.height())
    self.setMinimumSize(10, 10)
    self.setMaximumSize(self.playground.width(), self.playground.height())
    
    self.setGeometry(20, 40, self.playground.width(), self.playground.height())
    
    self.fishes = []
    
    self.show()
    
    self.timer = QtCore.QTimer(self)
    #QtCore.QObject.connect(self.timer, QtCore.SIGNAL('timeout()'), self.moveFishes)
    self.timer.timeout.connect(self.moveFishes)
    self.timer.start(10)
  
  def get_playground_width(self):
    return self.playground.width()

  def addFish(self, fish):
    self.fishes.append(fish)

  def moveFishes(self):
    self.random_pohyb = random.uniform(0, 100)
    self.pohne = True
    for fish in self.fishes:
      if(self.random_pohyb < 2 and self.pohne):
        fish.azimuth = random.uniform(0, 360)
        fish.velocity = random.uniform(1, 10)
        self.pohne = False
        fish.move(0.15)

      fish.move(0.15)
    self.update()
  
  def closeEvent(self, event):
    reply = QtWidgets.QMessageBox.question(self, 'Aquarium', "Do you really want to devitalize all those fishes?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    if reply == QtWidgets.QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()

  def paintEvent(self, event):
    painter = QtGui.QPainter()
    painter.begin(self)
    painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
    painter.setRenderHint(QtGui.QPainter.TextAntialiasing, True)
    painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
    painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
    
    rectangle = QtCore.QRectF(QtCore.QPoint(0, 0), QtCore.QSizeF(self.playground.width(), self.playground.height()))
    painter.drawPixmap(rectangle, self.playground, self.playground_rect)
    
    for fish in self.fishes:
      fish.draw(painter)
    
    painter.end()

def main():
  app = QtWidgets.QApplication(sys.argv)
  aquarium = Aquarium()
  aquarium.addFish(Fish("little_fish.png", aquarium))
  aquarium.addFish(Fish("medium_fish.png", aquarium))
  aquarium.addFish(Fish("big_fish.png", aquarium))
  aquarium.addFish(Fish("clown_fish.png", aquarium))
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
