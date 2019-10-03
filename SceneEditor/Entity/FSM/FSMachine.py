#!/usr/bin/python
# -*- coding: utf-8 -*-
from Entity.Function.Function import Function
from Entity.CopyScene.CopyScene import CopyScene
from Entity.CopyScene.CopySceneNormal import CopySceneNormal
from Entity.Variable.Variable.Variable import *

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
var_machine_data = Variable("MachineData", VarType.T_TABLE, {})
var_machine_state = Variable("machine_state", VarType.T_INT, 0)


def build_func_name(pre_name, index):
    return pre_name + "_" + str(index)


class FSMachine:
    __state_max: int = 0
    __func_list = []
    __variable_list = []
    __copy_scene = object()

    def __init__(self, copy_scene):
        self.__state_max = 0
        self.__func_list = []
        self.__variable_list = []
        self.__copy_scene = copy_scene

    def init_machine(self):
        self.__variable_list.append(var_machine_data)
        self.__variable_list.append(var_machine_state)

    def get_func_list(self):
        return self.__func_list

    def get_var_list(self):
        return self.__variable_list

    def add_machine_state(self):
        self.__state_max = self.__state_max + 1

    def refresh_machine_func(self):
        self.__func_list = []

        if self.__state_max <= 0:
            return

        register_fsm_fun = Function("RegisterFSMachine", {}, self.print_fsm_body)
        self.__func_list.append(register_fsm_fun)

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

    def print_fsm_body(self):
        print("MachineData = {")
        for i in range(self.__state_max):
            start_name = build_func_name("OnStart", i)
            tick_name = build_func_name("OnTick", i)
            end_name = build_func_name("OnEnd", i)
            print(str_machine_format, start_name, tick_name, end_name)
        print("}")


