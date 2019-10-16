#!/usr/bin/python
# -*- coding: utf-8 -*-
from Entity.Function.Function import Function
from Entity.Statement.Statement import *
from Entity.Variable.Variable.Variable import *
from Utils.NameUtils import *
from Entity.SEData import *

"""
延迟调用逻辑
"""


class DelayMachine:
    """
    常量定义
    """
    const_register_func_name = "DelayRegister"
    const_register_func_param = {"0": "func", "1": "delaytime"}
    const_unregister_func_name = "DelayUnRegister"
    const_unregister_func_param = {"0": "func"}
    const_tick_func_name = "TickDelay"
    const_tick_func_param = {"0": "elapse"}
    const_machine_data_name = "DelayData"
    """
    DelayHandlerData = 
    {
       {handler, table_param, delaytime},
    }
    """

    "变量定义"
    var_var_member_list = []
    var_func_list = []

    def __init__(self):
        self.init_machine()

    def init_machine(self):
        self.init_member()
        self.init_func()

    def init_member(self):
        var_machine_data = CSTable(self.const_machine_data_name)
        self.var_var_member_list.append(var_machine_data)

    def init_func(self):
        func_register = Function(self.const_register_func_name,
                                 self.const_register_func_param,
                                 self.register_func_body)
        self.var_func_list.append(func_register)

        func_unregister = Function(self.const_unregister_func_name,
                                   self.const_unregister_func_param,
                                   self.unregister_func_body)
        self.var_func_list.append(func_unregister)

        func_tick = Function(self.const_tick_func_name,
                             self.const_tick_func_param,
                             self.tick_func_body)
        self.var_func_list.append(func_tick)

    def register_func_body(self):
        pass

    def unregister_func_body(self):
        pass

    def tick_func_body(self):
        pass
