class Performance:
    def __init__(self, aPlayID, anAudience):
        self.playID = aPlayID
        self.audience = anAudience
        self. play = ""
        self.amount = 0
        self.volumeCredits = 0

    @staticmethod
    def decode(dct):
        if ('playID' in dct) & ('audience' in dct):
            return Performance(dct['playID'], dct['audience'])
        return dct