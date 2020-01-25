#! /usr/bin/env python3
# coding: utf-8

import os
import math

from PyQt5.QtWidgets import (QApplication,QMainWindow)

#from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor, QPen, QCursor

#from PyQt5.QtCore import Qt, QObject, QPoint, QRectF, QPointF, QSize

from src.ui.guard import Ui_BitGuards

#import resources.style as ss

TITLE = 'BitGuards'
#LOGO = ":/images/logo.png"

class GuardWindow(QMainWindow):
    """ Definition of a class """
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BitGuards()
        self.ui.setupUi(self) 
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(TITLE)	
    
    def GMenu(self):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = GuardWindow()
    window.show()
    app.exec_()
