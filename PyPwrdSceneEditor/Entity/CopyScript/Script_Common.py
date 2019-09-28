from Entity.CopyScript.ScriptBase import CopyScript
from Entity.Function.FunBase import FunctionEntity

class CopyScript_Common(CopyScript):
    #方法执行
    #{naem:functionentity}
    _funList = {}
    def __init__(self, scriptid, name):        
        CopyScript.__init__(self, scriptid, name)

    def AddFunc(self, funcEntity):
        self._funList[funcEntity.GetName()] = funcEntity

    def Print(self):
        print("--Start:CopyScript_Common")
        CopyScript._PrintDesc(self)
        for k,v in self._funList.items():
            v.Print(self._scriptid)


def test():
    csc = CopyScript_Common(100,"test")
    funcE = FunctionEntity(101, {1:"testFnc"})
    csc.AddFunc(funcE)
    csc.PrintScript()

#test()