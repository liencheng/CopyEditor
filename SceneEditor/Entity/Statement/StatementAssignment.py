#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
赋值语句
"""
from Entity.Statement.Statement import Statement


class StatementAssignment(Statement):
    __left = ""
    __right = ""

    def __init__(self, name, right_value):
        self.__left = name
        self.__right = right_value

    def print(self):
        ret = ""
        ret = ret + self.__left + " = " + str(self.__right)
        print(ret)

