#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity.CopyScene.CopyScene import *
from Entity.CopyScene.CopySceneNormal import CopySceneNormal
from Entity.Function.Function import Function
from Entity.Function.FunctionForeachPlayer import *
from Entity.Statement.Statement import *
from Entity.Statement.StatementAssignment import *
from Entity.Statement.StatementFsmNpc import *
from Entity.Statement.StatementReturn import *

from Define.EditorDefine import ScriptType
from Entity.Variable.Variable.Variable import *
from Entity.Machine.FSMachine import FSMachine
from Utils.NameUtils import *
from Entity.SEData import *


class SceneEditor:
    m_copyScript = ""

    def GetCopyScript(self):
        return self.m_copyScript

    def InitCopyScript(self, scriptid, name, type):
        set_script_id(scriptid)
        if type == ScriptType.T_BASE:
            self.m_copyScript = CopyScene(scriptid, name)
        if type == ScriptType.T_COMMON:
            self.m_copyScript = CopySceneNormal(scriptid, name)

    def PrintScript(self):
        print("--start,脚本编辑器")
        self.m_copyScript.print()


# 添加注释
if __name__ == "__main__":
    editor = SceneEditor()
    editor.InitCopyScript(1000, "s1000", ScriptType.T_COMMON)
    cEntity = editor.GetCopyScript()

    var_int_test = CSInt("int_test")
    cEntity.add_variable(var_int_test)

    var_double_test = CSDouble("double_test")
    cEntity.add_variable(var_double_test)

    var_string_test = CSString("string_test")
    cEntity.add_variable(var_string_test)

    var_table_test = CSTable(CopyScene.cs_player_data_name)
    CopyScene.cs_add_variable(var_table_test)

    var_table_npc = CSTable(CopyScene.cs_npc_data_name)
    CopyScene.cs_add_variable(var_table_npc)

    funArgs = {"arg1": "eplase"}

    funEntityTick = Function("OnCopySceneTick", funArgs)
    cEntity.add_function(funEntityTick)

    funArgs = {}
    funEntityOpen = Function("OnCopySceneOpen", funArgs)
    cEntity.add_function(funEntityOpen)
    fsm_npc_statement = StatementFsmNpc("C_CreateNpcWithGroup", {"0": "10001"})
    cEntity.add_variable(fsm_npc_statement.get_var_ret())
    funEntityOpen.add_statement(fsm_npc_statement)



    funArgs = {}
    funEntityCD = Function("CleanData", funArgs)

    var_list = cEntity.get_variable()
    for var in var_list:
        assignstate = StatementAssignment(var.get_name(), var.default_value())
        funEntityCD.add_statement(assignstate)

    cEntity.add_function(funEntityCD)

    funArgs = {"arg1": "obj"}
    funEntityEnter = Function("OnCopyScenePlayerEnter", funArgs)
    cEntity.add_function(funEntityEnter)

    doArgs = {"arg1": 1, "arg2": 2}
    doEntity = Statement("_FuncTest", doArgs)
    funEntityOpen.add_statement(doEntity)

    doArgs = {}
    do_entity = Statement("CleanData", doArgs)
    funEntityOpen.add_statement(do_entity)

    fsm = FSMachine(1000)
    "增加三种状态"
    fsm.add_machine_state()
    fsm.add_machine_state()
    fsm.add_machine_state()
    fsm.refresh_machine_func()
    cEntity.set_fsm(fsm)

    fe_player = FunctionForeachPlayer()
    fe_npc = FunctionForeachNpc()
    sl_player = FunctionSelectPlayer()
    sl_npc = FunctionSelectNpc()
    cEntity.add_function(fe_player)
    cEntity.add_function(fe_npc)
    cEntity.add_function(sl_npc)
    cEntity.add_function(sl_player)

    editor.PrintScript()
