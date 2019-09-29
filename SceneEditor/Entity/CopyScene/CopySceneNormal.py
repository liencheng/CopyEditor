from Entity.CopyScene.CopyScene import CopyScene
from Entity.Function.Function import Function

class CopySceneNormal(CopyScene):
    #方法执行
    #{naem:functionentity}
    _funList = {}
    def __init__(self, scriptid, name):        
        CopyScene.__init__(self, scriptid, name)

    def AddFunc(self, funcEntity):
        self._funList[funcEntity.GetName()] = funcEntity

    def Print(self):
        print("--Start:CopySceneNormal")
        CopyScene._PrintDesc(self)
        for k,v in self._funList.items():
            v.Print(self._scriptid)


def test():
    csc = CopySceneNormal(100, "test")
    funcE = Function(101, {1: "testFnc"})
    csc.AddFunc(funcE)
    csc.PrintScript()

#test()