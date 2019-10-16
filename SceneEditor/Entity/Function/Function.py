from Entity.Statement.Statement import Statement
from Entity.SEData import *

class Function:
    _name = ""
    _params = {}
    __statement_list = []
    __body_func_callback = object()

    def __init__(self, name, params_dict: object = {}, body_func_callback: object = object()) -> object:
        self._name = wrap_name(name)
        self._params = params_dict
        self.__statement_list = []
        self.__body_func_callback = body_func_callback

    def set_body_callback(self, callback):
        self.__body_func_callback = callback

    def GetName(self):
        return self._name

    def add_statement(self, statement):
        self.__statement_list.append(statement)

    def GetParams(self):
        return self._params

    def _PrintComment(self):
        print("")
        print("--")

    def print(self):
        self._PrintComment()
        fheader_pre = "function " + self._name + "("
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
