from Entity.Statement.Statement import Statement

class Function:
    _name = ""
    _params = {}
    __statement_list ={}

    def __init__(self, name, paramsDict):
        self._name = name
        self._params= paramsDict
        self.__statement_list.clear()

    def GetName(self):
        return self._name

    def add_statement(self, doEntity):
        self.__statement_list[doEntity.GetName()] = doEntity

    def GetParams(self):
        return self._params

    def _PrintComment(self):
       print("")
       print("--")

    def Print(self, scriptid):
        self._PrintComment()
        fheader_pre = "function " + str(scriptid) + "_" + self._name + "("
        fheader_fix = ")"
        f_ender = "end"

        assistCt = 0
        for key in self._params.keys():
            assistCt = assistCt + 1
            fheader_pre = fheader_pre + self._params[key]
            if(assistCt>=len(self._params)):
                break
            fheader_pre = fheader_pre + ","
        fheader_pre = fheader_pre + fheader_fix

        print(fheader_pre)

        for key in self.__statement_list.keys():
            self.__statement_list[key].print()

        print(f_ender)


