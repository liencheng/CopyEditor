from Entity.Statement.Statement import Statement


class Function:
    _name = ""
    _params = {}
    __statement_list = []
    __body_func_callback = object()

    def __init__(self, name, params_dict={}, body_func_callback=object()):
        self._name = name
        self._params = params_dict
        self.__statement_list = []
        self.__body_func_callback = body_func_callback

    def GetName(self):
        return self._name

    def add_statement(self, doEntity):
        self.__statement_list.append(doEntity)

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
            if (assistCt >= len(self._params)):
                break
            fheader_pre = fheader_pre + ","
        fheader_pre = fheader_pre + fheader_fix

        print(fheader_pre)

        if callable(self.__body_func_callback):
            self.__body_func_callback()

        for s in self.__statement_list:
            s.print()

        print(f_ender)
