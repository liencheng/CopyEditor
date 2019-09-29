
class CopyScene:
    _scriptid = 0
    _name = []
    _desc = ""

    def __init__(self, scriptid, name):
        self._name = name
        self._scriptid = scriptid

    def GetScriptId(self):
        return self._scriptid

    def GetName(self):
        return self._name

    def AddDesc(self, desc):
        self._name.append(desc)
   
    def _PrintDesc(self):
        for des in self._desc:
            print("--" + des)

    def Print(self):
        print("CopyScene")
