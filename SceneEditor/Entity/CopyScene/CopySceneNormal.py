from Entity.CopyScene.CopyScene import CopyScene
from Entity.Function.Function import Function

class CopySceneNormal(CopyScene):

    def __init__(self, scriptid, name):
        CopyScene.__init__(self, scriptid, name)

    def print(self):
        print("--Start:CopySceneNormal")
        self.pre_process_fsm()
        self.print_comment()
        self.print_variable()
        for k, v in self.get_function_list().items():
            v.print()


