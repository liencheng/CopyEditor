#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from UI.UISceneEditorView import *
from UI.UIView import *


class UIStatement(UIView):

    def __init__(self, statement_name, param):
        UIView.__init__(self, statement_name)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.lbl_name = None
        self.lbl_param_list = []
        self.btn_del = None
        self.setLayout(self.layout)
        self.init(statement_name, param)

    def init(self, statement_name, param):
        self.lbl_name = QLabel(statement_name)
        for key  in param.keys():
            p_value = str(param[key])
            lbl_p = QLabel(p_value)
            self.lbl_param_list.append(lbl_p)
        self.btn_del = QPushButton("delete")

        self.layout.addWidget(self.lbl_name)
        for i in self.lbl_param_list:
            self.layout.addWidget(i)
        self.layout.addWidget(self.btn_del)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = UIStatement("test", {"0": 0})
    wnd.show()
    sys.exit(app.exec_())

