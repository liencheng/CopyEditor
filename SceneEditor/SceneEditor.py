#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity.CopyScene.CopyScene import CopyScene
from Entity.CopyScene.CopySceneNormal import CopySceneNormal
from Entity.Function.Function import Function
from Entity.Statement.Statement import Statement
from Entity.Statement.StatementAssignment import StatementAssignment
from Define.EditorDefine import ScriptType
from Entity.Variable.Variable.Variable import *


class SceneEditor:
    m_copyScript = ""

    def GetCopyScript(self):
        return self.m_copyScript

    def InitCopyScript(self, scriptid, name, type):
        if type == ScriptType.T_BASE:
            self.m_copyScript = CopyScene(scriptid, name)
        if type == ScriptType.T_COMMON:
            self.m_copyScript = CopySceneNormal(scriptid, name)

    def PrintScript(self):
        print("--start,脚本编辑器")
        self.m_copyScript.Print()


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

    var_table_test = CSTable("table_test")
    cEntity.add_variable(var_table_test)

    funArgs = {"arg1": "eplase"}
    funEntityTick = Function("OnCopySceneTick", funArgs)
    cEntity.add_function(funEntityTick)

    funArgs = {}
    funEntityOpen = Function("OnCopySceneOpen", funArgs)
    cEntity.add_function(funEntityOpen)

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

    editor.PrintScript()
