import os
import math

from PyQt5.QtWidgets import (QApplication,QMainWindow)

#from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor, QPen, QCursor

#from PyQt5.QtCore import Qt, QObject, QPoint, QRectF, QPointF, QSize

#from ressources.ui import Ui_Fic

#import resources.style as ss

TITLE = 'GuardBits'
#LOGO = ":/images/logo.png"

class GuardWindow(QMainWindow):
    """ Definition of a class """
    def __init__(self):
        """ Initializes an object """
        QMainWindow.__init__(self)
        #self.setupUi(self)
        #self.setStyleSheet(ss.DEFAULT)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(TITLE)    	
    
    def GMenu(self):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    prep = GuardWindow()
    prep.show()
    app.exec_()
# --- last line
