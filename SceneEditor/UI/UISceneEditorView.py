#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
from UI.UIView import *


class UISceneEditorView(UIView, QWidget):

    def __init__(self, name):
        QWidget.__init__(self)
        UIView.__init__(self, name)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.name)
        self.resize(view_default_width, view_default_height)
        self.move(500, 500)
        self.show()



