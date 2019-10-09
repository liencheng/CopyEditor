#!/usr/bin/python
# -*- coding: utf-8 -*-
from Entity.Function.Function import Function
from Entity.Variable.Variable.Variable import *
from Utils.NameUtils import *

"""
副本状态机
local ScriptID_MachineIndex = 0

function  DefineMachine()
    local MachineData = {
    [0]  = {OnStart = OnStart_0, OnTick = OnTick_0, OnEnd = OnEnd_0},
    [1]  = {OnStart = OnStart_1, OnTick = OnTick_1, OnEnd = OnEnd_1},
    [2]  = {OnStart = OnStart_2, OnTick = OnTick_2, OnEnd = OnEnd_2},
    [3]  = {OnStart = OnStart_3, OnTick = OnTick_3, OnEnd = OnEnd_3},
    ...
    }

end

function OnStart_0()
end

function OnTick_0(elapse)
end

function OnEnd_0()
    ScriptID_MachineIndex = ScriptId_MachineIndex +1
end


function ScriptId_TickMachine(elapse)
    if MachineData[ScriptId_MachineIndex] ~= nil then
        MachineData[ScriptId_MachineIndex].OnTick(elapse)
    end
end
...
"""

str_machine_format = "OnStart = {0}, OnTick = {1}, OnEnd = {2},"
var_machine_data_name = "MachineData"
var_machine_data = Variable(var_machine_data_name, VarType.T_TABLE, {})
var_machine_state = Variable("machine_state", VarType.T_INT, 0)


def build_func_name(script_id, pre_name, index):
    ret = pre_name + "_" + str(index)
    return encode_func_name(script_id, ret)




class FSMachine:
    __state_max: int = 0
    __func_list = []
    __variable_list = []
    __script_id = 0

    def __init__(self, script_id):
        self.__state_max = 0
        self.__func_list = []
        self.__variable_list = []
        self.__script_id = script_id
        self.init_machine()

    def init_machine(self):
        self.__variable_list.append(var_machine_data)
        self.__variable_list.append(var_machine_state)

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

        register_fsm_fun = Function(encode_func_name(self.__script_id, "RegisterFSMachine"),
                                    {},
                                    self.fun_body_of_register_fsm)
        self.__func_list.append(register_fsm_fun)
        change_next_state_fun = Function(encode_func_name(self.__script_id, "Change2NextState"),
                                         {},
                                         self.fun_body_of_change_2_next_state)

        self.__func_list.append(change_next_state_fun)

        for i in range(self.__state_max):
            start_name = build_func_name(self.__script_id, "OnStart", i)
            start_func = Function(start_name)
            end_name = build_func_name(self.__script_id, "OnEnd", i)
            end_func = Function(end_name)
            tick_name = build_func_name(self.__script_id, "OnTick", i)
            params = {"p0": "elapse"}
            tick_func = Function(tick_name, params)

            self.__func_list.append(start_func)
            self.__func_list.append(end_func)
            self.__func_list.append(tick_func)

    def fun_body_of_register_fsm(self):
        print(var_machine_data_name)
        print("= {")
        for i in range(self.__state_max):
            start_name = build_func_name(self.__script_id, "OnStart", i)
            tick_name = build_func_name(self.__script_id, "OnTick", i)
            end_name = build_func_name(self.__script_id, "OnEnd", i)
            print(str_machine_format.format(start_name, tick_name, end_name))
        print("}")

    def fun_body_of_change_2_next_state(self):
        name = var_machine_state.get_name()
        ret = name + " = "
        ret = ret + name
        ret = ret + "+ 1"
        print(ret)


