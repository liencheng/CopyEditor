#!/usr/bin/python
# -*- coding: utf-8 -*-
from Define.EditorDefine import VarType
import Utils.VariableUtils
from Entity.SEData import *


class Variable:
    __name = ""
    __type = -1
    __default = ""

    def __init__(self, name, value_type, value_default):
        self.__name = wrap_name(name)
        self.__type = value_type
        self.__default = value_default

    def get_name(self):
        return self.__name

    def default_value(self):
        return self.__default

    def print(self):
        ret = Utils.VariableUtils.build_variable(self.__type, self.__name, self.__default)
        print(ret)
        return ret

    def init(self):
        ret = Utils.VariableUtils.build_variable_default(self.__name, self.__default)
        print(ret)
        return ret


class CSNumberal(Variable):
    def __init__(self, name):
        Variable.__init__(self, name, VarType.T_NUMBER, 0)


class CSInt(CSNumberal):
    def __init__(self, name):
        Variable.__init__(self, name, VarType.T_INT, 0)


class CSDouble(CSNumberal):
    def __init__(self, name):
        Variable.__init__(self, name, VarType.T_DOUBLE, 0)


class CSString(Variable):
    def __init__(self, name):
        Variable.__init__(self, name, VarType.T_STRING, "\"\"")


class CSTable(Variable):
    def __init__(self, name):
        Variable.__init__(self, name, VarType.T_TABLE, {})
