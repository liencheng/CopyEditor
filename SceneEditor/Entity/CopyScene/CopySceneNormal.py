from Entity.CopyScene.CopyScene import CopyScene
from Entity.Function.Function import Function

class CopySceneNormal(CopyScene):
    #方法执行
    __funList = {}

    def __init__(self, scriptid, name):
        CopyScene.__init__(self, scriptid, name)

    def add_function(self, funcEntity):
        self.__funList[funcEntity.GetName()] = funcEntity

    def Print(self):
        print("--Start:CopySceneNormal")
        self._PrintDesc()
        self.print_variable()
        for k, v in self.__funList.items():
            v.Print(self._script_id)


def test():
    csc = CopySceneNormal(100, "test")
    funcE = Function(101, {1: "testFnc"})
    csc.add_function(funcE)
    csc.PrintScript()

#test()