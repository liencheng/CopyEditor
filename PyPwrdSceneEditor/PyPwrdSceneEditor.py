from Entity.CopyScript.ScriptBase import CopyScript
from Entity.CopyScript.Script_Common import CopyScript_Common
from Entity.Function.FunBase import FunctionEntity
from Entity.Executor.ExeBase import DoEntity

class PwrdSceneEditor:
    m_copyScript = ""

    def GetCopyScript(self):
        return self.m_copyScript

    def InitCopyScript(self, scriptid, name, type):
        if type == 0:
            self.m_copyScript = CopyScript(scriptid, name)

        if type == 1:
            self.m_copyScript = CopyScript_Common(scriptid, name)

    def PrintScript(self):
        print("--start,脚本编辑器")
        self.m_copyScript.Print()



if __name__ =="__main__":
    editor = PwrdSceneEditor()
    editor.InitCopyScript(1000, "s1000", 1)
    cEntity = editor.GetCopyScript()
    
    funArgs = {"arg1":"eplase"}
    funEntity = FunctionEntity("OnCopySceneTick", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1":"obj"}
    funEntity = FunctionEntity("OnCopyScenePlayerEnter", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1":"obj"}
    funEntity = FunctionEntity("OnCopyScenePlayerLevel", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1":"obj"}
    funEntity = FunctionEntity("OnCopyScenePlayerDie", funArgs)
    cEntity.AddFunc(funEntity)

    funArgs = {"arg1":"obj"}
    funEntity = FunctionEntity("OnCopySceneNpcDie", funArgs)
    cEntity.AddFunc(funEntity)


    doArgs = {"arg1":1}
    doEntity = DoEntity("_FuncTest", doArgs)
    
    funEntity.AddDoEntity(doEntity)

    editor.PrintScript()