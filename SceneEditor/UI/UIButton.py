#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from UI.UISceneEditorView import *
from UI.UIView import *


class UIButton(QPushButton):

    def __init__(self, name):
        QPushButton.__init__(self, name)
        self.resize(200, 200)
        self.init(name)

    def init(self, name):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    btn = UIButton("btn")
    btn.show()
    sys.exit(app.exec_())
