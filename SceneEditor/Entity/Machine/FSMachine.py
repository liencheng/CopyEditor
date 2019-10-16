#!/usr/bin/python
# -*- coding: utf-8 -*-
from Entity.Function.Function import Function
from Entity.Statement.Statement import *
from Entity.Variable.Variable.Variable import *
from Utils.NameUtils import *
from Entity.SEData import *


str_machine_format = "OnStart = {0}, OnTick = {1}, OnEnd = {2},"
var_machine_data_name = "MachineData"
str_onstart_func_format = "if nil ~= {0}.[{1}] and nil ~= {2}.[{3}].OnStart then"
str_onstart_func_format_0 = "{0}.[{1}].OnStart()"
str_onend_func_format = "if nil ~= {0}.[{1}] and nil ~= {2}.[{3}].OnEnd then"
str_onend_func_format_0 = "{0}.[{1}].OnEnd()"
str_ontick_func_format = 'if nil ~= {0}.[{1}] and nil ~= {2}.[{3}].OnTick then'
str_ontick_func_format_0 = "{0}.[{1}].OnTick(elapse)"


def build_func_name(pre_name, index):
    ret = pre_name + "_" + str(index)
    return ret


class FSMachine:
    __state_max: int = 0
    __func_list = []
    __variable_list = []
    __script_id = 0
    __var_machine_data: Variable = None
    __var_machine_state: Variable = None

    def __init__(self, script_id):
        self.__state_max = 0
        self.__func_list = []
        self.__variable_list = []
        self.__script_id = script_id
        self.__var_machine_data = Variable(var_machine_data_name, VarType.T_TABLE, {})
        self.__var_machine_state = Variable("machine_state", VarType.T_INT, 0)
        self.init_machine()

    def init_machine(self):
        self.__variable_list.append(self.__var_machine_data)
        self.__variable_list.append(self.__var_machine_state)

    def get_func_list(self):
        return self.__func_list

    def get_var_list(self):
        return self.__variable_list

    def add_machine_state(self):
        self.__state_max = self.__state_max + 1
        self.refresh_machine_func()

    def refresh_machine_func(self):
        self.__func_list = []

        if self.__state_max <= 0:
            return

        onstart_fun = Function("OnStart", {}, self.fun_body_of_on_start)
        onend_fun = Function("OnEnd", {}, self.fun_body_of_on_end)
        ontick_fun = Function("OnTick", {"0": "elapse"},
                              self.fun_body_of_on_tick)
        self.__func_list.append(onstart_fun)
        self.__func_list.append(onend_fun)
        self.__func_list.append(ontick_fun)

        register_fsm_fun = Function("RegisterFSMachine",
                                    {},
                                    self.fun_body_of_register_fsm)
        self.__func_list.append(register_fsm_fun)

        inc_fsm_state_fun = Function("IncFsmState",
                                     {},
                                     self.fun_body_of_change_2_next_state)
        self.__func_list.append(inc_fsm_state_fun)

        change_2_next_state_fuc = Function("Change2NextState")
        inc_fsm_state_statement = Statement(inc_fsm_state_fun.GetName(), {})
        onstart_statement = Statement(onstart_fun.GetName(), {})
        onend_statement = Statement(onend_fun.GetName(), {})
        change_2_next_state_fuc.add_statement(onend_statement)
        change_2_next_state_fuc.add_statement(inc_fsm_state_statement)
        change_2_next_state_fuc.add_statement(onstart_statement)
        self.__func_list.append(change_2_next_state_fuc)

        for i in range(self.__state_max):
            start_name = build_func_name("OnStart", i)
            start_func = Function(start_name)
            end_name = build_func_name("OnEnd", i)
            end_func = Function(end_name)
            tick_name = build_func_name("OnTick", i)
            params = {"p0": "elapse"}
            tick_func = Function(tick_name, params)

            self.__func_list.append(start_func)
            self.__func_list.append(end_func)
            self.__func_list.append(tick_func)

    def fun_body_of_register_fsm(self):
        print(var_machine_data_name)
        print("= {")
        for i in range(self.__state_max):
            start_name = build_func_name("OnStart", i)
            tick_name = build_func_name("OnTick", i)
            end_name = build_func_name("OnEnd", i)
            print(str_machine_format.format(start_name, tick_name, end_name))
        print("}")

    def fun_body_of_change_2_next_state(self):
        name = self.__var_machine_state.get_name()
        ret = name + " = "
        ret = ret + name
        ret = ret + "+ 1"
        print(ret)

    """
    if nil ~= MachineData[state] and nil ~= MachineData[State].OnStart then
        MachineData[State].OnStart()
    end
    """
    def fun_body_of_on_start(self):
        machine_data_name = self.__var_machine_data.get_name()
        machine_index = self.__var_machine_state.get_name()
        str_if_head = str_onstart_func_format.format(machine_data_name, machine_index, machine_data_name, machine_index)
        str_if_body = str_onstart_func_format_0.format(machine_data_name, machine_index)
        print(str_if_head)
        print(str_if_body)
        print("end")


    def fun_body_of_on_end(self):
        machine_data_name = self.__var_machine_data.get_name()
        machine_index = self.__var_machine_state.get_name()
        str_if_head = str_onend_func_format.format(machine_data_name, machine_index, machine_data_name, machine_index)
        str_if_body = str_onend_func_format_0.format(machine_data_name, machine_index)
        print(str_if_head)
        print(str_if_body)
        print("end")

    def fun_body_of_on_tick(self):
        machine_data_name = self.__var_machine_data.get_name()
        machine_index = self.__var_machine_state.get_name()
        str_if_head = str_ontick_func_format.format(machine_data_name, machine_index, machine_data_name, machine_index)
        str_if_body = str_ontick_func_format_0.format(machine_data_name, machine_index)
        print(str_if_head)
        print(str_if_body)
        print("end")
