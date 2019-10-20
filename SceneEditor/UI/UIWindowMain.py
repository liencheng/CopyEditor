#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import  QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from UI.UISceneEditorView import *
from UI.UIButton import *
from UI.UIStatement import *


class UIWindowMain(QWidget):
    se_view = None
    layout = None

    def __init__(self):
        QWidget.__init__(self)
        self.resize(1000, 1000)
        self.move(300, 300)
        self.setWindowTitle("UIWindowMain")
        self.layout = QHBoxLayout()
        self.layout.addWidget(QPushButton("main_btn"))
        self.setLayout(self.layout)

        s = UIStatement("create_npc", {"0": 10001, "1": 10002})
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.alignment()
        layout.addWidget(s)
        view_widget = UIView("uiView")
        view_widget.setLayout(layout)
        #view_widget.setLayout(layout)
        #layout.addWidget(QPushButton("uiview:btn"))
        #s.layout.addWidget(QPushButton("sbtn"))

        self.layout.addWidget(view_widget)

    def init_ui(self):
        pass

    def add_widget(self, widget):
        self.layout.addChildWidget(widget)




app = QApplication(sys.argv)
wnd = UIWindowMain()
wnd.show()

sys.exit(app.exec_())

