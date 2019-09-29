#!/usr/bin/python
# -*- coding: utf-8 -*-
from Entity.CopyScene.CopyScene import CopyScene
from Entity.CopyScene.CopySceneNormal import CopySceneNormal
from Entity.Function.Function import Function
from Entity.Statement.Statement import Statement
from Define.EditorDefine import ScriptType


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


if __name__ == "__main__":
    editor = SceneEditor()
    editor.InitCopyScript(1000, "s1000", ScriptType.T_COMMON)
    cEntity = editor.GetCopyScript()
    
    funArgs = {"arg1": "eplase"}
    funEntity = Function("OnCopySceneTick", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopyScenePlayerEnter", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopyScenePlayerLevel", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopyScenePlayerDie", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1": "obj"}
    funEntity = Function("OnCopySceneNpcDie", funArgs)
    cEntity.AddFunc(funEntity)

    doArgs = {"arg1": 1, "arg2": 2}
    doEntity = Statement("_FuncTest", doArgs)
    funEntity.add_statement(doEntity)
    editor.PrintScript()
