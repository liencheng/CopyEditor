#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
含有return语句
"""

from Entity.Statement.Statement import *
from Entity.Variable.Variable.Variable import *


class StatementReturn(Statement):
    _b_global_var: bool = False
    _var_ret: Variable = None

    def __init__(self, b_global, ret_var, statement_name, params):
        Statement.__init__(statement_name, params)
        self._b_global_var = b_global
        self._var_ret = ret_var

    def get_var_ret(self):
        return self._var_ret

    def b_is_global_ret(self):
        return self._b_global_var

    def get_text(self):
        output = ""
        base_output = Statement.get_text(self)
        if self._b_global_var:
            output = ""
        else:
            output = "local "
        output = output + self._var_ret.get_name()
        output = output + " = "
        output = output + base_output
        return output

    def print(self):
        output = self.get_text()
        print(output)


