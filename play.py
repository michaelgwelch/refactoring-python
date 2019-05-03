class Play:
    def __init__(self, aName, aType):
        self.name = aName
        self.type = aType

    @staticmethod
    def decode(dct):
        if ("name" in dct) & ("type" in dct):
            return Play(dct['name'], dct['type'])
        return dct