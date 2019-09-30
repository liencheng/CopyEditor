#!/usr/bin/python
# -*- coding: utf-8 -*-
from Entity.CopyScene.CopyScene import CopyScene
from Entity.CopyScene.CopySceneNormal import CopySceneNormal
from Entity.Function.Function import Function
from Entity.Statement.Statement import Statement
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


#添加注释
if __name__ == "__main__":
    editor = SceneEditor()
    editor.InitCopyScript(1000, "s1000", ScriptType.T_COMMON)
    cEntity = editor.GetCopyScript()

    var_int_test = CSInt("test")
    cEntity.add_variable(var_int_test)

    funArgs = {"arg1": "eplase"}
    funEntity = Function("OnCopySceneTick", funArgs)
    cEntity.add_function(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopyScenePlayerEnter", funArgs)
    cEntity.add_function(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopyScenePlayerLevel", funArgs)
    cEntity.add_function(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopyScenePlayerDie", funArgs)
    cEntity.add_function(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopySceneNpcDie", funArgs)
    cEntity.add_function(funEntity)

    doArgs = {"arg1": 1, "arg2": 2}
    doEntity = Statement("_FuncTest", doArgs)
    funEntity.add_statement(doEntity)
    editor.PrintScript()
