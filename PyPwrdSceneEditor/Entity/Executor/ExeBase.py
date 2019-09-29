class DoEntity:
    _name = ""
    _params = {}

    def __init__(self, name, paramsDict):
        self._name = name
        self._params= paramsDict

    def GetName(self):
        return self._name

    def GetParams(self):
        return self._params


    def Print(self):
        output = self._name +"("
        bFirst = True
        for key in self._params.keys():
            if (bFirst == True):
                output = output + str(self._params[key])
            else:
                output = output + "," + str(self.__params[key])
        print("name")

class DE_CallBack(DoEntity):
    callback = ""
    def __init__(self, name, paramsDict, callback):
        self.callback = callback
        super.__init__(self, name, paramsDict)