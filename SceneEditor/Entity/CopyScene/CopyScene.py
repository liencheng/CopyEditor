
from Entity.Variable.Variable.Variable import Variable

class CopyScene:

    __script_id = 0
    __name = ""
    __desc = ""
    __variable_list = []

    def __init__(self, scriptid, name):
        self.__name = name
        self.__script_id = scriptid

    def add_variable(self, var: bool):
        self.__variable_list.append(var)

    def get_variable(self):
        return self.__variable_list

    def GetScriptId(self):
        return self.__script_id

    def GetName(self):
        return self.__name

    def AddDesc(self, desc):
        self.__name.append(desc)
   
    def _PrintDesc(self):
        for des in self.__desc:
            print("--" + des)

    def Print(self):
        print("CopyScene")

    def print_variable(self):
        for i in self.__variable_list:
            i.print(self.__script_id)

