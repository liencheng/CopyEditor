
from Entity.Variable.Variable.Variable import Variable
from Entity.Machine.FSMachine import FSMachine


class CopyScene:
    "静态常亮"
    cs_player_data_name = "player_data"
    cs_npc_data_name = "npc_data"
    "静态方法"
    static_variable_list: Variable = []
    "成员方法"
    _script_id = 0
    __name = ""
    __desc = ""
    __variable_list = []
    "状态机"
    __fsm:FSMachine = None
    "方法执行"
    __funList = {}

    def __init__(self, scriptid, name):
        self.__name = name
        self._script_id = scriptid
        self.__fsm = None

    def add_variable(self, var: Variable):
        self.__variable_list.append(var)

    def get_variable(self):
        return self.__variable_list

    def get_fsm(self):
        return self.__fsm

    def set_fsm(self, fsm):
        self.__fsm = fsm

    def del_fsm(self):
        self.__fsm = None

    def add_function(self, funcEntity):
        self.__funList[funcEntity.GetName()] = funcEntity

    def get_function_list(self):
        return self.__funList

    def GetScriptId(self):
        return self._script_id

    def GetName(self):
        return self.__name

    def AddDesc(self, desc):
        self.__name.append(desc)
   
    def print_comment(self):
        for des in self.__desc:
            print("--" + des)

    def print(self):
        print("CopyScene")

    def print_variable(self):
        for i in CopyScene.static_variable_list:
            i.print()
        for i in self.__variable_list:
            i.print()

    def pre_process_fsm(self):
        if self.__fsm:
            fsm_var = self.__fsm.get_var_list()
            fsm_fun = self.__fsm.get_func_list()

            for i in fsm_var:
                self.add_variable(i)

            for i in fsm_fun:
                self.add_function(i)

    @staticmethod
    def cs_add_variable(var: Variable):
        CopyScene.static_variable_list.append(var)

    @staticmethod
    def cs_get_player_data() -> object:
        for i in CopyScene.static_variable_list:
            if i.get_raw_name() == CopyScene.cs_player_data_name:
                return i
        return None

    @staticmethod
    def cs_get_npc_data() -> object:
        for i in CopyScene.static_variable_list:
            if i.get_raw_name() == CopyScene.cs_npc_data_name:
                return i
        return None

