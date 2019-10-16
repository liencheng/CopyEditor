#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
常方法：
    function ForeachPlayer(trait_func)
    end
    function SelectPlayer(trait_func)
    end
"""

from Entity.Function.Function import *
from Entity.CopyScene.CopyScene import *

foreach_player_fun_name = "ForeachPlayer"
foreach_npc_fun_name = "ForeachNpc"
select_player_fun_name = "SelectPlayer"
select_npc_fun_name = "SelectNpc"
foreach_player_param_name = "traverse_player"
foreach_npc_param_name = "traverse_npc"
select_player_param_name = "select_player"
select_npc_param_name = "select_npc"
body_format_0 = "for i, v in pair({0}) do"
body_format_1 = "{0}(v[1])"
body_format_2 = "end"
body_format_3 = "if true == {0}(v[1]) then return end"


class FunctionForeachPlayer(Function):

    def __init__(self):
        Function.__init__(self, foreach_player_fun_name, {"p0": foreach_player_param_name},
                          FunctionForeachPlayer.body_callback)

    @staticmethod
    def body_callback():
        var_player_data: Variable = CopyScene.cs_get_player_data()
        if var_player_data is None:
            print("function_foreach_player error.")
            return
        body_0 = ""
        body_0 = body_0 + body_format_0.format(var_player_data.get_name())
        body_1 = body_format_1.format(foreach_player_param_name)
        body_2 = body_format_2
        print(body_0)
        print(body_1)
        print(body_2)


class FunctionForeachNpc(Function):

    def __init__(self):
        Function.__init__(self, foreach_npc_fun_name, {"p0": foreach_npc_param_name}, FunctionForeachNpc.body_callback)

    @staticmethod
    def body_callback():
        var_npc_data: Variable = CopyScene.cs_get_npc_data()
        if var_npc_data is None:
            print("error:function_foreach_player error.")
            return
        body_0 = ""
        body_0 = body_0 + body_format_0.format(var_npc_data.get_name())
        body_1 = body_format_1.format(foreach_npc_param_name)
        body_2 = body_format_2
        print(body_0)
        print(body_1)
        print(body_2)


class FunctionSelectPlayer(Function):

    def __init__(self):
        Function.__init__(self, select_player_fun_name, {"p0": select_player_param_name}, FunctionSelectPlayer.body_callback)

    @staticmethod
    def body_callback():
        var_player_data: Variable = CopyScene.cs_get_player_data()
        if var_player_data is None:
            print("function_foreach_player error.")
            return
        body_0 = ""
        body_0 = body_0 + body_format_0.format(var_player_data.get_name())
        body_1 = body_format_3.format(select_player_param_name)
        body_2 = body_format_2
        print(body_0)
        print(body_1)
        print(body_2)

class FunctionSelectNpc(Function):

    def __init__(self):
        Function.__init__(self, select_npc_fun_name, {"p0": select_npc_param_name}, FunctionSelectNpc.body_callback)

    @staticmethod
    def body_callback():
        var_npc_data: Variable = CopyScene.cs_get_npc_data()
        if var_npc_data is None:
            print("error:function_foreach_player error.")
            return
        body_0 = ""
        body_0 = body_0 + body_format_0.format(var_npc_data.get_name())
        body_1 = body_format_3.format(select_npc_param_name)
        body_2 = body_format_2
        print(body_0)
        print(body_1)
        print(body_2)


