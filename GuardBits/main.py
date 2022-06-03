#! /usr/bin/env python3
# coding: utf-8

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit)

from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor, QPen, QCursor

# from PyQt5.QtCore import Qt, QObject, QPoint, QRectF, QPointF, QSize

from src.ui.guard import Ui_BitGuards
from src.ui.login import Ui_LoginWindow

# import ressources.style as ss
import src.inc.constants as ct


class GuardWindow(QMainWindow):
    """ Guard main window of the application"""
    def __init__(self):
        QMainWindow.__init__(self)
        self.auth = False
        if self.auth:
            self.ui = Ui_BitGuards()
            self.ui.setupUi(self)
            self.bitGuards_init()
        else:
            self.ui = Ui_LoginWindow()
            self.ui.setupUi(self)
            self.login_init()

    def bitGuards_init(self):
        self.setWindowTitle(ct.TITLE)
        self.setContentsMargins(0, 0, 0, 0)
        self.centralWidget().setContentsMargins(0, 0, 0, 0)
        self.centralWidget().layout().setContentsMargins(0, 0, 0, 0)
        # self.setWindowIcon(QIcon(ct.LOGO))
        # self.setStyleSheet(ss)
        #self.listMenu.setModel()

    def login_init(self):
        self.setWindowTitle(ct.TITLE_LOGIN)
        self.setContentsMargins(0, 0, 0, 0)
        self.centralWidget().setContentsMargins(0, 0, 0, 0)
        self.centralWidget().layout().setContentsMargins(0, 0, 0, 0)
        #self.leLogin.setPlaceholderText("Login")
        self.lePassword.setPlaceholderText("Password")
        self.lePassword.setEchoMode(QLineEdit.Password)
        self.btnLogin.clicked.connect(self.auth_platform)

    def auth_platform(self):
        print(self.leLogin.text())
        print(self.lePassword.text())

    def init_ui(self):
        self.pbAdd.clicked.connect(self.add_bits)

    def add_bits(self):
        print("add bits")

    def gMenu(self):
        print("menu")


# --------------------------------------------------------


#class gbModel(QStandardItemModel):
#    def __init__(self):
#        gbModel.__init__(self)


# --------------------------------------------------------

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = GuardWindow()
    window.show()
    app.exec_()
