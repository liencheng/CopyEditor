from Entity.Statement.Statement import Statement

class Function:
    _name = ""
    _params = {}
    _dolist ={}

    def __init__(self, name, paramsDict):
        self._name = name
        self._params= paramsDict
        self._dolist.clear()

    def GetName(self):
        return self._name

    def AddDoEntity(self, doEntity):
        self._dolist[doEntity.GetName()] = doEntity

    def GetParams(self):
        return self._params

    def _PrintComment(self):
       print("")
       print("--")

    def Print(self, scriptid):

        self._PrintComment()

        fheaderPre = "function " + str(scriptid) + "_" + self._name + "(" 
        fheaderFix = ")"
        fEnder = "end"

        assistCt = 0
        for key in self._params.keys():
            assistCt = assistCt + 1
            fheaderPre = fheaderPre + self._params[key]
            if(assistCt>=len(self._params)):
                break
            fheaderPre = fheaderPre + ","
        fheaderPre = fheaderPre + fheaderFix

        print(fheaderPre)

        for key in self._dolist.keys():
            self._dolist[key].Print()

        print(fEnder)


