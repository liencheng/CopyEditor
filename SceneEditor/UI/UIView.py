#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget

view_default_height = 500
view_default_width = 500


class UIView(QWidget):

    def __init__(self, name):
        QWidget.__init__(self)
        self.name = name

    def get_name(self):
        return self.name



