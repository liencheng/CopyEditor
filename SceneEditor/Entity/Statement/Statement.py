class Statement:
    _name = ""
    _params = {}

    def __init__(self, name, paramsDict):
        self._name = name
        self._params= paramsDict

    def get_name(self):
        return self._name

    def GetParams(self):
        return self._params

    def print(self):
        output = self._name +"("
        b_first = True
        for key in self._params.keys():
            if b_first:
                output = output + str(self._params[key])
                b_first = False
            else:
                output = output + "," + str(self._params[key])
        output = output + ")"
        print(output)

